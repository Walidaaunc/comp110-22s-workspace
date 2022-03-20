"""Dictionary related utility functions."""
__author__ = "730507751"
# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Opens a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepares to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    # Reads each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file when we're done, to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first `N` rows of data for each column."""
    result: dict[str, list[str]] = dict()
    res = next(iter(table))
    for column in table[res]:
        wanted_list: list[int] = list()
        for value in column:
            result[value] = wanted_list.append(N)
        print(wanted_list)
    return result


def select(table: dict[str, list[str]], name_of_column: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = dict()
    for column in name_of_column:
        result[column] = table[column]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = dict()
    for column in table_one:
        result[column] = table_one[column]
    for column in table_two:
        if column in result:
            result[column] += table_two[column]
        else:
            result[column] = table_two[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Given a list of str, this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = dict()
    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result