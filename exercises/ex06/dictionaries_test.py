"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730396458"


def test_invert_edge() -> None:
    """Use an empty dictionary."""
    totest: dict[str, str] = {}
    assert invert(totest) == {}


def test_invert_repeat() -> None:
    """Have another use case."""
    totest: dict[str, str] = {'a': 'b', 'd': 'd', '2': '1'}
    assert invert(totest) == {'b': 'a', 'd': 'd', '1': '2'}


def test_invert_use() -> None:
    """A normal use with a multi key dictionary."""
    totest: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(totest) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_favorite_color_edge() -> None:
    """The edge case."""
    start: dict[str, str] = {}
    assert favorite_color(start) == {}
 

def test_favorite_color_many() -> None:
    """A different use case with many choices."""
    choices: dict[str, str] = {'Kay': 'blue', 'Greg': 'blue', 'Kate': "orange", "Meg": 'purple'}
    assert favorite_color(choices) == 'blue'
    

def test_favorite_color_use() -> None:
    """A use case with few choices."""
    choices: dict[str, str] = {'Mike': 'grey', 'Meg': 'blue'}
    assert favorite_color(choices) == 'grey'


def test_count_edge() -> None:
    """Edge case for count."""
    new_list: list[str] = []
    assert count(new_list) == {}


def test_count_use() -> None:
    """Use case with repetition."""
    one: list[str] = ['h', 'e', 'l', 'l', 'o', 'o']
    assert count(one) == {'h': 1, 'e': 1, 'l': 2, 'o': 2}


def test_count_single() -> None:
    """Use case with one object."""
    one: list[str] = ["lol"]
    assert count(one) == {"lol": 1}