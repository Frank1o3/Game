""" entity.py """
from vector import Vector2
from shape import Shape


class Entity:
    """Class representing a physical entity in the simulation."""

    def __init__(self, shape: Shape, mass: float = 1.0):
        self.shape = shape
        self.velocity = Vector2(0, 0)
        self.mass = mass

    def update(self):
        """Move the shape based on velocity."""
        center = getattr(self.shape, "center", None)
        if center is not None:
            center.add(self.velocity)
        else:
            position = getattr(self.shape, "position", None)
            if position is not None:
                position.add(self.velocity)
