"""Writing a test subject of the invert, count, and favorite_colors functions."""
__author__ = "730507751"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values of a dictionary."""
    new_dictionary: dict[str, str] = dict()
    for key in a:
        if a[key] in new_dictionary:
            raise KeyError
        new_dictionary[a[key]] = key
    return new_dictionary    


def favorite_color(a: dict[str, str]) -> str:
    """Returns a str of the color that appears most frequently in a given dictionary."""
    the_valued_string: str = ""
    new_list: list[str] = list()
    for key in a:
        color: str = a[key]
        new_list.append(color)
    new_dictionary: dict[str, int] = dict()
    for value in new_list:
        if value in new_dictionary:
            new_dictionary[value] += 1
        else:
            new_dictionary[value] = 1
    value_max: int = 0
    for values in new_dictionary:
        if value_max < new_dictionary[values]:
            value_max = new_dictionary[values]
            the_valued_string = values
    return the_valued_string


def count(a: list[str]) -> dict[str, int]:
    """Produces a dictionary where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    the_dictionary: dict[str, int] = dict()
    for key in a:
        if key in the_dictionary:
            the_dictionary[key] += 1
        else:
            the_dictionary[key] = 1
    return the_dictionary