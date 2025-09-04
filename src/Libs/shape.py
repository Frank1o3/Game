"""shapes.py"""
from vector import Vector2


class Shape:
    """ Base class for shapes """

    def intersects(self, other: 'Shape') -> bool:
        """ Check if this shape intersects with another shape """
        raise NotImplementedError


class Circle(Shape):
    """ Circle shape """

    def __init__(self, center: Vector2, radius: float, static: bool = False):
        self.center = center
        self.radius = radius
        self.static = static  # New attribute to indicate if the rectangle is static

    def intersects(self, other: 'Shape') -> bool:
        if isinstance(other, Circle):
            return self.center.distance_to(other.center) < (self.radius + other.radius)
        elif isinstance(other, Rectangle):
            # Clamp point to rectangle and check circle distance
            closest_x = max(other.position.x, min(
                self.center.x, other.position.x + other.width))
            closest_y = max(other.position.y, min(
                self.center.y, other.position.y + other.height))
            dist = Vector2(self.center.x - closest_x,
                           self.center.y - closest_y).length()
            return dist < self.radius
        return False  # polygon case later


class Rectangle(Shape):
    """ Rectangle shape """

    def __init__(self, position: Vector2, width: float, height: float, static: bool = False):
        self.position = position  # top-left
        self.width = width
        self.height = height
        self.static = static  # New attribute to indicate if the rectangle is static

    def intersects(self, other: 'Shape') -> bool:
        if isinstance(other, Rectangle):
            return (self.position.x < other.position.x + other.width and
                    self.position.x + self.width > other.position.x and
                    self.position.y < other.position.y + other.height and
                    self.position.y + self.height > other.position.y)
        elif isinstance(other, Circle):
            return other.intersects(self)  # use circle’s logic
        return False
