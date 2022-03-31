from __future__ import annotations

from typing import Union


class strArray:
    items: list[str]

    def __init__(self, items):
        self.items = items
    
    def __repr__(self) -> str:
        return f"strArray({self.items})"
    
    def __add__(self, rhs: Union[str, strArray]) -> strArray:
        """Add is a vectorized operation that applies to all items. When rhs is a str, it is concatenated to every item in a new StrArray."""
        result: list[str] = list()
        if isinstance(rhs, str):
            for item in self.items:
                result.append(item + rhs)
        else:
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
        return strArray(result)
        

first: strArray = strArray(["Armando", "Brady", "Caleb"])
last: strArray = strArray(["Bacot", "Manek", "Love"])
print(first + "!")
print(first + last)
print(last + ", " + first)
print(first + "//" + last)