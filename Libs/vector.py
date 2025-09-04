""" Vector2 class """
from typing import Optional
import math


class Vector2:
    """ 2D Vector class """

    def __init__(self, x=0.0, y=0.0) -> None:
        self.x = float(x)
        self.y = float(y)

    def add(self, x: Optional['float|Vector2'] = None, y: float = 0.0) -> 'Vector2':
        """ Add a vector or x and y values to this vector """
        if isinstance(x, Vector2):
            self.x += x.x
            self.y += x.y
        elif x:
            self.x += x
            self.y += y
        return self

    def sub(self, x: Optional['float|Vector2'] = None, y: float = 0.0) -> 'Vector2':
        """ Subtract a vector or x and y values from this vector """
        if isinstance(x, Vector2):
            self.x -= x.x
            self.y -= x.y
        elif x:
            self.x -= x
            self.y -= y
        return self

    def mul(self, x: Optional['float|Vector2'] = None, y: float = 0.0) -> 'Vector2':
        """ Multiply this vector by a vector or x and y values """
        if isinstance(x, Vector2):
            self.x *= x.x
            self.y *= x.y
        elif x:
            self.x *= x
            self.y *= y
        return self

    def div(self, x: Optional['float|Vector2'] = None, y: float = 0.0) -> 'Vector2':
        """ Divide this vector by a vector or x and y values """
        try:
            if isinstance(x, Vector2):
                if x.x != 0:
                    self.x /= x.x
                if x.y != 0:
                    self.y /= x.y
            elif x:
                if x != 0:
                    self.x /= x
                if y != 0:
                    self.y /= y
        except ZeroDivisionError:
            pass
        return self

    def length(self) -> float:
        """ Get the length of this vector """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self) -> 'Vector2':
        """ Normalize this vector """
        length = self.length()
        if length != 0:
            self.x /= length
            self.y /= length
        return self

    def distance_to(self, other: 'Vector2') -> float:
        """ Get the distance to another vector """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
