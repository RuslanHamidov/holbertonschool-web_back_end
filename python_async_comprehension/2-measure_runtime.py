#!/usr/bin/env python3
"""measure_runtime coroutine
that will execute async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio
import time
import random
from typing import List, Generator

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''async function that returns runtime of 4 async_comp'''
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(),async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
