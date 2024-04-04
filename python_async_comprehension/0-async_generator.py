#!/usr/bin/env python3
''' async generator '''

import random
import asyncio
from typing import Generator


async def async_generator():
    async for i in range(0,10):
        await asyncio.sleep(1)
        n = random.randint(0,10)
        return
