""" engine.py """
from threading import Thread, Event
from queue import Queue
from typing import List
from entity import Entity


class Engine:
    """A simple physics engine simulation class."""
    GRAVITY = 9.81  # m/s^2
    thread_count = 4  # The number of threads to use for processing
    stop_event = Event()

    def __init__(self):
        self.entities = Queue()  # Queue to hold entities for processing
        self.time_step = 0.016
        self.current_time = 0.0

    def worker(self):
        """Worker function to update a list of entities."""
        while not self.stop_event.is_set():
            # If not doing anything get the Entity from the queue
            entity = self.entities.get()
            if entity is None and not isinstance(entity, Entity):
                break

            if getattr(entity.shape, "static", False):
                # Apply gravity to the entity's velocity
                entity.velocity.add(y=self.GRAVITY * self.time_step)

            # Collision handling
            self.collision(entity)

            entity.update()
            self.entities.task_done()

    def run(self) -> None:
        """Run the physics engine."""
        threads: List[Thread] = []
        for _ in range(self.thread_count):
            thread = Thread(target=self.worker)
            thread.start()
            threads.append(thread)

        try:
            while True:
                self.current_time += self.time_step
                self.entities.join()  # Wait for all entities to be processed
        except KeyboardInterrupt:
            self.stop_event.set()
            for _ in threads:
                self.entities.put(None)

    def add_entity(self, entity: Entity) -> None:
        """Add an entity to the engine."""
        if isinstance(entity, Entity):
            self.entities.put(entity)
        else:
            raise TypeError(
                "Only Entity instances can be added to the engine.")

    def collision(self, entity: Entity) -> None:
        """Handle collisions between entities."""
        for other in list(self.entities.queue):
            if other is entity or not isinstance(other, Entity):
                continue
            if entity.shape.intersects(other.shape):
                # Simple elastic bounce on y-axis
                entity.velocity.y *= -1 * \
                    (entity.mass / (entity.mass + other.mass))
                other.velocity.y *= -1 * \
                    (other.mass / (entity.mass + other.mass))
