"""List utility functions part 2."""

__author__ = "730396458"


def only_evens(xs: list[int]) -> list[int]:
    i: int = 0
    evens: list[int] = list()
    while i < len(xs):
        if (xs[i] / 2) == (xs[i] // 2):
            evens.append(xs[i])
        i += 1
    return evens
