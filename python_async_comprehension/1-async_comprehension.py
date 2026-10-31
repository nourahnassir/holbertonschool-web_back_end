#!/usr/bin/env python3
"""
A module containing an asynchronous comprehension coroutine.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronously collects 10 random numbers from async_generator
    using an async comprehension and returns them.
    """
    return [i async for i in async_generator()]
