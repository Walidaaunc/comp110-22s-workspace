"""Writing a test subject of the only_evens, sub, and concat functions."""
__author__ = "730507751"


def only_evens(the_given_list: list[int]) -> list[int]:
    """Returns a list containing only the elements of the input list that were even."""
    new_list: list[int] = list()
    i: int = 0
    while i < len(the_given_list):
        if the_given_list[i] % 2 == 0:
            new_list.append(the_given_list[i])
        i += 1
    return new_list


def sub(the_given_list: list[int], a: int, b: int) -> list[int]:
    """Generates a List which is a subset of the given list, between the specified start index and the end index - 1."""
    new_list: list[int] = list()
    if a < 0:
        a = 0
    elif b > len(the_given_list):
        b = len(the_given_list)
    elif len(the_given_list) == 0:
        a = 1 + len(the_given_list)
    while a < b:
        new_list.append(the_given_list[a])
        a += 1
    return new_list


def concat(the_first_given_list: list[int], the_second_given_list: list[int]) -> list[int]:
    """Generates a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    new_list: list[int] = list()
    i: int = 0
    while i < len(the_first_given_list):
        new_list.append(the_first_given_list[i])
        i += 1
    i = 0
    while i < len(the_second_given_list):
        new_list.append(the_second_given_list[i])
        i += 1
    return new_list