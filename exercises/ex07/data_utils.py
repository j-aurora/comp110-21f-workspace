"""Utility functions."""

__author__ = "730396458"

# Define your function.

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
        section: list[str] = []
        while len(section) < limit:
            i: int = 0
            the_key: str = data[key][i]
            section.append(the_key)
            i += 1
        partial[key] = section
    return partial


def select(para1: dict[str, list[str]], para2: list[str]) -> dict[str, list[str]]:
    """Only displays selected categories of a table."""
    to_return: dict[str, list[str]] = {}
    for key in para2:
        to_return[key] = para1[key]

    return to_return


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    combined: dict[str, list[str]] = {}
    for key in first:
        combined[key] = first[key]
    for key in second:
        combined[key] = second[key]
    return combined


def count(par: list[str]) -> dict[str, int]:
    """Count the number of times something appears in a list."""
    the_count: dict[str, int] = {}
    for item in par:
        if item in the_count:
            the_count[item] += 1

    return the_count