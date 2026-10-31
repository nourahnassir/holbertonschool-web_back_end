#!/usr/bin/env python3
"""
A module defining a measure_runtime coroutine that executes
async_comprehension four times in parallel using asyncio.gather
and measures the total runtime.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel
    using asyncio.gather, measures the total runtime, and returns it.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
