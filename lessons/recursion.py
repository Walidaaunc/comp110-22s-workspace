from __future__ import annotations

from typing import Union, Optional


class Node:
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Union[Node, None]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next


def sum(node: Optional[Node]) -> int:
    if node is None:
        return 0
    else:
        return node.data + sum(node.next)

    
def __str__(self) -> str:
    if self.next is None:
        return f"{self.data} -> None"
    else:
        return f"{self.data} -> {self.next.__str__()}"


def count(node: Optional[Node], current_count: int = 0) -> int:
    if node is None:
        return current_count + 1
    else:
        return count(node.next, current_count + 1)


head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)
print(sum(head))
print(count(head))
print(head)