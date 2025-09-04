""" A simple physics engine simulation """
from threading import Thread, Event
from queue import Queue, Empty
from typing import List
from entity import Entity


class Engine:
    """A simple physics engine simulation class."""
    GRAVITY = 9.81  # m/s^2
    thread_count = 4
    stop_event = Event()

    def __init__(self, time_step: float = 0.016):
        self.entities: List[Entity] = []
        self.queue: Queue[Entity | None] = Queue()
        self.time_step = time_step
        self.current_time = 0.0
        self.threads: List[Thread] = []

    def worker(self):
        """Worker function to update entities."""
        while not self.stop_event.is_set():
            try:
                entity = self.queue.get(timeout=0.1)
            except Empty:
                continue

            if entity is None or not isinstance(entity, Entity):
                self.queue.task_done()
                break

            # Apply gravity if not static
            if not getattr(entity.shape, "static", False):
                entity.velocity.add(0, self.GRAVITY * self.time_step)

            # Handle collisions
            self.collision(entity)

            # Update position
            entity.update()

            self.queue.task_done()

    def run(self) -> None:
        """Run the physics engine."""
        # Start worker threads
        for _ in range(self.thread_count):
            t = Thread(target=self.worker, daemon=True)
            t.start()
            self.threads.append(t)

        try:
            while not self.stop_event.is_set():
                self.current_time += self.time_step
                # Dispatch entities to workers
                for entity in self.entities:
                    self.queue.put(entity)

                self.queue.join()
        except KeyboardInterrupt:
            self.stop()

    def stop(self) -> None:
        """Stop the physics engine."""
        self.stop_event.set()
        for _ in self.threads:
            self.queue.put(None)
        for t in self.threads:
            t.join()

    def add_entity(self, entity: Entity) -> None:
        """Register an entity with the engine."""
        self.entities.append(entity)

    def collision(self, entity: Entity) -> None:
        """Handle collisions between entities (very simplified)."""
        for other in self.entities:
            if other is entity:
                continue
            if entity.shape.intersects(other.shape):
                # Simple elastic bounce along y-axis
                total_mass = entity.mass + other.mass
                entity.velocity.y *= -other.mass / total_mass
                other.velocity.y *= -entity.mass / total_mass
