#!/usr/bin/env python3
"""Task 9 module"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with the length
     of each element in the input list"""
    return [(i, len(i)) for i in lst]
