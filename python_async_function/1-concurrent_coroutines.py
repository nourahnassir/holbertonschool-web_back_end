#!/usr/bin/env python3
"""
A module containing an asynchronous routine that spawns
wait_random n times with a specified max_delay.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawns wait_random n times with the specified max_delay
    and returns the list of all delays in ascending order.
    """
    delays = []
    for coroutine in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delay = await coroutine
        delays.append(delay)
    return delays
