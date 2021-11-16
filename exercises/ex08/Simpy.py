"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730396458"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialization of attributes."""
        self.values = values
    
    def __repr__(self) -> str:
        """Produce a str representation of Simpy for Python."""
        return f"Simpy({self.values})"

    def __str__(self) -> str:
        """Convert values into a str representation."""
        return f"Simpy({self.values}) "
    
    def fill(self, to_fill: float, how_many: int) -> None:
        """Fill a simpy's values with repeating values."""
        self.values = [] 
        i: int = 0
        while i < how_many:
            self.values.append(to_fill)
            i += 1
       
    def arange(self, start: float, stop: float, step: float = 1.0):
        """Create another range of values."""
        self.values = []
        assert step != 0.0
        # if step is positive loop
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step
        if step < 0.0:
            neg_value: float = start
            while neg_value > stop:
                self.values.append(neg_value)
                neg_value += step
    
    def sum(self) -> float:
        """Delegate to the sum function."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload additon operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload exponentiation operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result