#!/usr/bin/env python3
"""
A module containing an asynchronous routine that creates tasks
using task_wait_n.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Takes n and max_delay, spawns task_wait_random n times,
    and returns the list of all delays in ascending order.
    """
    delays = []
    for coroutine in asyncio.as_completed(
        [task_wait_random(max_delay) for _ in range(n)]
    ):
        delay = await coroutine
        delays.append(delay)
    return delays
