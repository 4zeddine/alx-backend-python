#!/usr/bin/env python3
"""Task 1. Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    """Wait n times for a random delay between 0 and max_delay"""
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
