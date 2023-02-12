from typing import Any
from itertools import product

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    new = []
    for i in range(min(len(arr1), len(arr2))):
        new.append((arr1[i], arr2[i]))
    return new
