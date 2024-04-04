#!/usr/bin/env python3
''' async generator '''

import random
import asyncio


async def async_generator():
    '''async generator'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0,10)

async def main():
    async for number in async_generator():
        print(number)

# Run the main coroutine
asyncio.run(main())
