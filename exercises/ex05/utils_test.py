"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730396458"


def test_evens_empty() -> None:
    """Use empty list."""
    xs: list[int] = []
    assert only_evens(xs) == [] 


def test_evens_one() -> None:
    """Use odd number."""
    xs: list[int] = [1]
    assert only_evens(xs) == [] 


def test_evens_two() -> None:
    """Inlcude an even number."""
    xs: list[int] = [1, 2]
    assert only_evens(xs) == [2]


def test_evens_case() -> None:
    """Using long list of many numbers."""
    xs: list[int] = [1, 2, 3, 5, 6, 40, 41, 45, 56]
    assert only_evens(xs) == [2, 6, 40, 56] 


def test_sub_ex() -> None:
    """Empty list."""
    sub_list: list[int] = []
    assert sub(sub_list, 1, 3) == []


def test_sub_negstart() -> None:
    """Test a negative start index."""
    sub_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(sub_list, -4, 5) == [1, 2, 3, 4, 5]


def test_sub_largend() -> None:
    """Test end index greater than list."""
    sub_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(sub_list, 2, 11) == [3, 4, 5, 6, 7]


def test_sub_zerostart() -> None:
    """Start index is 0."""
    sub_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(sub_list, 0, 5) == [1, 2, 3, 4, 5]


def test_concat_single() -> None:
    """Empty lists."""
    one: list[int] = []
    two: list[int] = []
    assert concat(one, two) == []


def test_concat_without() -> None:
    """Use one empty list."""
    one: list[int] = [10, 11]
    two: list[int] = []
    assert concat(one, two) == [10, 11]


def test_concat_longer() -> None:
    """Use longer lists."""
    one: list[int] = [2, 4, 6, 8, 10]
    two: list[int] = [20, 40, 80]
    assert concat(one, two) == [2, 4, 6, 8, 10, 20, 40, 80]