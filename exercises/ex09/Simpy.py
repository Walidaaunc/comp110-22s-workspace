"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730507751"


class Simpy:
    values: list[float]

    def __init__(self, a: list[float]):
        """Construction definition for initialization of attributes."""
        self.values = a
    
    def __str__(self) -> str:
        """Produce a str representation of Simpy."""
        return f"Simpy({self.values})"
    
    def fill(self, filling_value: float, amount_of_times: int) -> None:
        """Mutates the object by filling the object's values with the filling_value for the stated amount_of_times."""
        new_list: list[float] = list()
        i: int = 0
        while i < amount_of_times:
            new_list.append(filling_value)
            i += 1
        self.values = new_list
    
    def arange(self, start: float, stop: float, step = 1.0) -> None:
        if step != 1.0:
            index: float = step
        else:
            index: float = 1.0
        new_list: list[float] = list()
        if stop > 0.0:
            while start < stop:
                new_list.append(start)
                start += index
            self.values = new_list
        else:
            while start > stop:
                new_list.append(start)
                start += index
            self.values = new_list
    
    def sum(self) -> float:
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        if isinstance(rhs, Simpy):
            if len(self.values) == len(rhs.values):
                new_simpy_object: Simpy
                new_list: list[float] = list()
                index: float = 0.0
                i: int = 0
                while i < len(self.values):
                    index = self.values[i] + rhs.values[i]
                    new_list.append(index)
                    index = 0.0
                    i += 1
                new_simpy_object = Simpy(new_list)
            return new_simpy_object
        elif isinstance(rhs, float):
            new_simpy_object: Simpy
            new_list: list[float] = list()
            index: float = 0.0
            i: int = 0
            while i < len(self.values):
                index = self.values[i] + rhs
                new_list.append(index)
                index = 0.0
                i += 1
            new_simpy_object = Simpy(new_list)
            return new_simpy_object
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        if isinstance(rhs, Simpy):
            if len(self.values) == len(rhs.values):
                new_simpy_object: Simpy
                new_list: list[float] = list()
                index: float = 0.0
                i: int = 0
                while i < len(self.values):
                    index = self.values[i] ** rhs.values[i]
                    new_list.append(index)
                    index = 0.0
                    i += 1
                new_simpy_object = Simpy(new_list)
            return new_simpy_object
        elif isinstance(rhs, float):
            new_simpy_object: Simpy
            new_list: list[float] = list()
            index: float = 0.0
            i: int = 0
            while i < len(self.values):
                index = self.values[i] ** rhs
                new_list.append(index)
                index = 0.0
                i += 1
            new_simpy_object = Simpy(new_list)
            return new_simpy_object
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        if isinstance(rhs, Simpy):
            new_list: list[bool] = list()
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    new_list.append(True)
                    i += 1
                else:
                    new_list.append(False)
                    i += 1
            return new_list
        elif isinstance(rhs, float):
            new_list: list[bool] = list()
            for value in self.values:
                if value == rhs:
                    new_list.append(True)
                else:
                    new_list.append(False)
            return new_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        if isinstance(rhs, Simpy):
            new_list: list[bool] = list()
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    new_list.append(True)
                    i += 1
                else:
                    new_list.append(False)
                    i += 1
            return new_list
        elif isinstance(rhs, float):
            new_list: list[bool] = list()
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    new_list.append(True)
                    i += 1
                else:
                    new_list.append(False)
                    i += 1
            return new_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        if isinstance(rhs, int):
            if len(self.values) > rhs:
                return self.values[rhs]
            else:
                raise IndexError
        else:
            returned_object: list[float] = list()
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    returned_object.append(self.values[i])
                i += 1
            return Simpy(returned_object)