#!/usr/bin/env python3
"""Task 7 module."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of a string and a float.
    Args:
        k (str): a string.
        v (Union[int, float]): an int or a float.
    Returns:
        Tuple[str, float]: a tuple of a string and a float.
    """
    return k, v * v
