""" 2D Vector class """
from __future__ import annotations
import math
from typing import Union


class Vector2:
    """2D Vector class"""

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = float(x)
        self.y = float(y)

    def add(self, x: Union[float, Vector2] = 0.0, y: float = 0.0) -> Vector2:
        """Add a vector or (x, y) values to this vector"""
        if isinstance(x, Vector2):
            self.x += x.x
            self.y += x.y
        else:
            self.x += float(x)
            self.y += float(y)
        return self

    def sub(self, x: Union[float, Vector2] = 0.0, y: float = 0.0) -> Vector2:
        """Subtract a vector or (x, y) values from this vector"""
        if isinstance(x, Vector2):
            self.x -= x.x
            self.y -= x.y
        else:
            self.x -= float(x)
            self.y -= float(y)
        return self

    def mul(self, x: Union[float, Vector2] = 1.0, y: float = 1.0) -> Vector2:
        """Multiply this vector by a vector or (x, y) values"""
        if isinstance(x, Vector2):
            self.x *= x.x
            self.y *= x.y
        else:
            self.x *= float(x)
            self.y *= float(y)
        return self

    def div(self, x: Union[float, Vector2] = 1.0, y: float = 1.0) -> Vector2:
        """Divide this vector by a vector or (x, y) values"""
        if isinstance(x, Vector2):
            if x.x != 0:
                self.x /= x.x
            if x.y != 0:
                self.y /= x.y
        else:
            if x != 0:
                self.x /= float(x)
            if y != 0:
                self.y /= float(y)
        return self

    def length(self) -> float:
        """Get the length of this vector"""
        return math.hypot(self.x, self.y)

    def normalize(self) -> Vector2:
        """Normalize this vector"""
        length = self.length()
        if length != 0:
            self.x /= length
            self.y /= length
        return self

    def distance_to(self, other: Vector2) -> float:
        """Get the distance to another vector"""
        return math.hypot(self.x - other.x, self.y - other.y)

    def copy(self) -> Vector2:
        """Return a copy of this vector"""
        return Vector2(self.x, self.y)

    def __repr__(self) -> str:
        return f"Vector2({self.x:.3f}, {self.y:.3f})"
