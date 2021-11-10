"""Example of a Point Class."""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float):
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Immutable: multiplies components by factor without mutation."""
        return Point(self.x * factor, self.y * factor)

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator."""
        print("__mul__ was called.")
        return Point(self.x * factor, self.y * factor)

    def __str__(self) -> str:
        """Produce a str representation of a Point for humans."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python."""
        return f"Point({self.x}, {self.y})"

    def __add__(self, rhs: Point) -> Point:
        """Overload additon operator."""
        print("__add_ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Apply index to the point."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else: 
            raise IndexError

a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])

p0: Point = Point(1.0, 2.0)
p1: Point = p0.scale(2.0)
print(p0)
pl_as_a_str: str = str(p1)
print(pl_as_a_str)

p1_repr: str = repr(p1)
print(p1_repr)