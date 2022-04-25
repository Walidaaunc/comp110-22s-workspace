"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730507751"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], given_number: int = 0) -> int:
    """Given a head Optional[Node] and an index int as inputs, the value_at function returns the data of the Node stored at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif given_number == 0:
        return head.data
    else:
        return value_at(head.next, given_number - 1)


def max(head: Optional[Node]) -> int:
    """Given a head Node, the max function returns the maximum data value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        if head.next is None:
            return head.data
        else:
            if head.data >= max(head.next):
                return head.data
            return max(head.next)


def linkify(items: list[int]) -> Optional[Node]:
    """Given a list[int], the linkify function returns a Linked List of Nodes with the same values, in the same order, as the input list."""
    if items == []:
        return None
    else:
        data: int = items[0]
        items.pop(0)
        return Node(data, linkify(items))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Given a head Node of a linked list and a int factor to scale by, the scale function returns a new linked list of Nodes where each value in the original list is scaled by the scaling factor."""
    if head is None:
        return None
    elif head.next is None:
        return Node(head.data * factor, None)
    else:
        return Node(head.data * factor, scale(head.next, factor))