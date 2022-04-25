"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, scale, value_at, max, is_equal, linkify

__author__ = "730507751"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value_at of an empty Linked List should raise an IndexError."""
    with pytest.raises(IndexError):
        value_at(None)


def test_value_at_non_empty() -> None:
    """Value_at of a non-empty list should return the data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_max_empty() -> None:
    """Max of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Max of a non-empty list should return the data value."""
    linked_list = (Node(10, Node(30, Node(20, None))))
    assert max(linked_list) == 30


def test_linkify_empty() -> None:
    """Linkify of an empty Linked List should return None."""
    list_object: list[int] = []
    assert is_equal(linkify(list_object), None)


def test_linkify_not_empty() -> None:
    """Linkify of a non-empty Linked List should return a Linked List of Nodes with the same values, in the same order."""
    object: list[int] = [1, 2, 3]
    assert is_equal(linkify(object), (Node(1, Node(2, Node(3, None)))))


def test_scale_empty() -> None:
    """Scale of an empty Node should return None."""
    assert scale(None, 1) is None


def test_scale_not_empty() -> None:
    """Scale of a non-empty Node should return a new linked list of Nodes where each value in the original list is scaled by the scaling factor."""
    object: Node = (Node(1, Node(2, Node(3, None))))
    assert is_equal(scale(object, 2), (Node(2, Node(4, Node(6, None)))))