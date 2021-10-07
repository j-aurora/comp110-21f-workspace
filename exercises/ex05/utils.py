"""List utility functions part 2."""

__author__ = "730396458"


def only_evens(xs: list[int]) -> list[int]:
    """Return only even numbers in the list."""
    i: int = 0
    evens: list[int] = list()
    while i < len(xs):
        if (xs[i] / 2) == (xs[i] // 2):
            evens.append(xs[i])
        i += 1
    return evens


def sub(sub_list: list[int], start: int, end: int) -> list[int]:
    """Return list with values between given indices."""
    index_list: list[int] = []
    i: int = 0
    d: int = len(sub_list) 
    if d > end:
        d = end 
    if start <= 0:
        while i < d:
            index_list.append(sub_list[i])
            i += 1
        return index_list
    if start > 0: 
        i = start
        while i < d:
            index_list.append(sub_list[i])
            i += 1
        return index_list 


def concat(first: list[int], second: list[int]) -> list[int]:
    """Return input lists as one."""
    junto: list[int] = list()
    i: int = 0
    while i < len(first):
        junto.append(first[i])
        i += 1
    p: int = 0
    while p < len(second):
        junto.append(second[p])
        p += 1
    return junto