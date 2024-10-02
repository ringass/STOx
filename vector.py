from __future__ import annotations
import math

class Vector2D():
    def __init__(self,
                 x = 0.0,
                 y = 0.0
    ):
        self.X = x
        self.Y = y

    def __add__(self, other: Vector2D) -> Vector2D:
        ret = Vector2D(self.X, self.Y)

        ret.X += other.X
        ret.Y += other.Y

        return ret

    def __sub__(self, other: Vector2D) -> Vector2D:
        ret = Vector2D(self.X, self.Y)

        ret.X -= other.X
        ret.Y -= other.Y

        return ret

    def __mul__(self, other: float|int) -> Vector2D:

        ret = Vector2D(self.X, self.Y)
        ret.X = ret.X * other
        ret.Y = ret.Y * other

        return ret

    def __div__(self, other: float|int) -> Vector2D:
        ret = Vector2D(self.X, self.Y)
        ret.X = ret.X / other
        ret.Y = ret.Y / other

        return ret

    def __neg__(self) -> Vector2D:
        ret = Vector2D(-self.X, -self.Y)
        return ret

    def __abs__(self) -> float:
        return math.sqrt(self.X**2 + self.Y**2)

    def __str__(self) -> str:
        return "({},{})".format(self.X, self.Y)
    
    def __eq__(self, other: Vector2D) -> bool:
        return self.X == other.X and self.Y == other.Y 

    def to_tuple(self) -> tuple[Vector2D, Vector2D]:
        return (self.X, self.Y)
    
    def from_polar(abs: float, angle: float) -> Vector2D:
        ret = Vector2D(math.cos(angle)*abs, math.sin(angle)*abs)
        return ret