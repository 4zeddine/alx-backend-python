#!/usr/bin/python3
"""Task 8 module."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a multiplier.
    Args:
        multiplier (float): a float.
    Returns:
        Callable[[float], float]: a function that multiplies a float by a multiplier.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
