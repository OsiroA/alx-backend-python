#!/usr/bin/env python3
"""
Task 1's module.
"""
from typing import List

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Creates a list of 10 numbers from a 10-number generator.
    """
    return [value async for value in async_generator()]
