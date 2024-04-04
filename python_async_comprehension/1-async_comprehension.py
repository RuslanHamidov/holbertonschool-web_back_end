#!/usr/bin/env python3
"""The coroutine will collect 10 random numbers 
using an async comprehensing over async_generator, 
then return the 10 random numbers.
"""

import asyncio
import random
from typing import List, Generator

async_generator = __import__('0-basic_async_syntax').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    '''async function returns list of random numbers'''
    list_of_float: List[float] = []
    list_of_float.append([async_generator async for _ in range(10)])
    return list_of_float
        