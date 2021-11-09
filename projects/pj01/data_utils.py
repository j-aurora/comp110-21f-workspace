"""Utility functions."""

__author__ = "730396458"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into a 'table'."""
    result: list[dict[str, str]] = []

# Open a handle to the data file.
    file_handle = open(filename, "r", encoding="utf8")
    
# Prepare to read the data file as CSV instead of strings.
    csv_reader = DictReader(file_handle)

# Read each row of the CSV line by line
    for row in csv_reader:
        result.append(row)

    # CLose file when done to free its resources()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented tabled."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result 


def head(data: dict[str, list[str]], limit: int) -> dict[str, list[str]]:
    """Will show the first few rows of a column oriented table."""
    partial: dict[str, list[str]] = {}
    for key in data:
        partial[key] = []
    for key in data: 
        section: list[str] = []
        while len(section) < limit:
            i: int = 0
            section.append(data[key][i])
            i += 1
        partial[key] = section
    return partial


def select(para1: dict[str, list[str]], para2: list[str]) -> dict[str, list[str]]:
    """Only displays selected categories of a table."""
    to_return: dict[str, list[str]] = {}
    for key in para2:
        to_return[key] = para1[key]

    return to_return


def difficulty(numbers: list[str]) -> list[str]:
    """Convert str objects of ratings into int objects and categorize as 'easy' or 'difficult'."""
    ratings: list[int] = []
    i: int = 0
    while i < len(numbers):
        ratings.append(int(numbers[i]))
        i += 1
    diff_rate: list[str] = []
    d: int = 0
    while d < len(ratings):
        if ratings[d] < 4:
            diff_rate.append('easy')
        else:
            diff_rate.append('difficult')
        d += 1

    return diff_rate


def sort_experience(all_exp: list[str]) -> list[str]:
    """Categorize experience levels."""
    diff_rate: list[str] = []
    d: int = 0
    while d < len(all_exp):
        if all_exp[d] == "7-12 months" or all_exp[d] == "1-2 years" or all_exp[d] == "Over 2 years":
            diff_rate.append('more')
        else:
            diff_rate.append('little')
        d += 1

    return diff_rate


def count(par: list[str]) -> dict[str, int]:
    """Count how many times a thing appears in a list."""
    the_count: dict[str, int] = {}
    for item in par:
        the_count[item] = 1
    for item in par: 
        if item in the_count:
            the_count[item] += 1

    return the_count


def bar_graph(numbs: list[str], categories: list[str]) -> list[str]:
    """Make a new list of ratings that are also categorized as 'easy'."""
    new_set: list[str] = []
    i: int = 0
    while i < len(numbs):
        if categories[i] == "more":
            new_set.append(numbs[i])
        i += 1
    return new_set