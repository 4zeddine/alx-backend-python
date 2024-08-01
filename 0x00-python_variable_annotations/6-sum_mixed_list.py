#!/usr/bin/env python3
"""Task 5 module."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum a list of ints and floats.
    Args:
        mxd_lst (List[Union[int, float]]): a list of ints and floats:
    Returns:
        float: the sum of the ints and floats in the list.
    """
    return sum(mxd_lst)
