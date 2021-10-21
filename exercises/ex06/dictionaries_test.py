"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730396458"


def test_invert_edge() -> None:
    """Use an empty dictionary."""
    totest: dict[str, str] = {}
    assert invert(totest) == {}


def test_invert_repeat() -> None:
    """Have a repeated key."""


def test_invert_use() -> None:
    "A normal use with a multi key dictionary."
    totest: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(totest) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_fav_edge() -> None:
    """The edge case."""
    start: dict[str, str] = {}
    assert favorite_color(start) == {}
 

def test_fav_many() -> None:
    """A different use case with many choices."""
    choices: dict[str, str] = {'Kay': 'blue', 'Greg': 'blue', 'Kate': "orange", "Meg": 'purple'}
    assert favorite_color(choices) == 'blue'
    

def test_fav_use() -> None:
    """A use case with few choices."""
    choices: dict[str, str] = {'Mike': 'grey', 'Meg': 'blue'}
    assert favorite_color(choices) == 'grey'


def test_count_edge() -> None:
    """Edge case for count."""
    new_list: list[str] = []
    assert count(new_list) == {}


def test_count_use() -> None:
    one: list[str] = ['h', 'e', 'l', 'l', 'o', 'o']
    assert count(one) == {'h': 1, 'e': 1, 'l': 2, 'o': 2}


def test_count_single() -> None:
    one: list[str] = ["lol"]
    assert count(one) == {"lol": 1}