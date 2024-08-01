#!/usr/bin/env python3
"""Task 11 module."""
from typing import Union, Any, TypeVar, Mapping


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Return dct[key] if it exists, otherwise return default."""
    if key in dct:
        return dct[key]
    else:
        return default
