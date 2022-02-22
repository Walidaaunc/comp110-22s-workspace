"""Tests for the only_evens, sub, and concat functions."""
__author__ = "730507751"
from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests for an edge case for the only_evens function."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_many_items_one() -> None:
    """Tests for a use case for the only_evens function."""
    xs: list[int] = [2, 4]
    assert only_evens(xs) == [2, 4]


def test_only_evens_many_items_two() -> None:
    """Tests for a second use case for the only_evens function."""
    xs: list[int] = [1, 3, 5, 6]
    assert only_evens(xs) == [6]


def test_sub_single_item() -> None:
    """Tests for an edge case for the sub function."""
    xs: list[int] = [1]
    assert sub(xs, 0, 1) == [1]


def test_sub_many_items_one() -> None:
    """Tests for a use case for the sub function."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_many_items_two() -> None:
    """Tests for a second use case for the sub function."""
    xs: list[int] = [5, 7]
    assert sub(xs, 0, 2) == [5, 7]


def test_concat_one_empty_list() -> None:
    """Tests for an edge case for the concat function."""
    xs: list[int] = []
    xy: list[int] = [2]
    assert concat(xs, xy) == [2]


def test_concat_full_lists_one() -> None:
    """Tests for a use case for the concat function."""
    xs: list[int] = [1, 2, 3]
    xy: list[int] = [4, 5, 6]
    assert concat(xs, xy) == [1, 2, 3, 4, 5, 6]


def test_concat_full_lists_two() -> None:
    """Tests for a second use case for the concat function."""
    xs: list[int] = [10, 100]
    xy: list[int] = [1000]
    assert concat(xs, xy) == [10, 100, 1000]