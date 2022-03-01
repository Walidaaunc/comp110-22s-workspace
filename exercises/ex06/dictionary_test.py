"""Tests for the invert, count, and favorite_colors functions."""
__author__ = "730507751"
from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests for an edge case for the invert function."""
    xs: dict[str, str] = {"": "Ball"}
    assert invert(xs) == {"Ball": ""}


def test_invert_many_items_one() -> None:
    """Tests for a use case for the invert function."""
    xs: dict[str, str] = {"Owen": "Boy", "Nick": "Man"}
    assert invert(xs) == {"Boy": "Owen", "Man": "Nick"}


def test_invert_many_items_two() -> None:
    """Tests for a second use case for the invert function."""
    xs: dict[str, str] = {"Kanye": "Goat", "Presley": "Meh", "Jackson": "Cool"}
    assert invert(xs) == {"Goat": "Kanye", "Meh": "Presley", "Cool": "Jackson"}


def test_favorite_color_many_items_empty() -> None:
    """Tests for an edge case for the favorite_color function."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_favorite_color_many_items_one() -> None:
    """Tests for a use case for the favorite_color function."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_many_items_two() -> None:
    """Tests for a second use case for the favorite_color function."""
    xs: dict[str, str] = {"Walid": "Green", "Bruh": "Red"}
    assert favorite_color(xs) == "Green"


def test_count_empty() -> None:
    """Tests for an edge case for the count function."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_many_items_one() -> None:
    """Tests for a use case for the count function."""
    xs: list[str] = ["Apple", "Apple", "Bees"]
    assert count(xs) == {"Apple": 2, "Bees": 1}


def test_count_many_items_two() -> None:
    """Tests for a second use case for the count function."""
    xs: list[str] = ["Goku", "Vegeta", "Beerus", "Goku", "Beerus", "Beerus"]
    assert count(xs) == {"Goku": 2, "Vegeta": 1, "Beerus": 3}