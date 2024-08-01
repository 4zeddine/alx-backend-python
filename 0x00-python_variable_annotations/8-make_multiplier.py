#!/usr/bin/python3
"""Task 8 module."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a multiplier.
    """
    return lambda x: x * multiplier
