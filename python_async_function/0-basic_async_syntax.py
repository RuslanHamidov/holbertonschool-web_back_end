#!/usr/bin/env python3
'''
coroutine that takes in an integer argument (max_delay, with a default value of 10)
named wait_random that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
'''

import random, asyncio
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int,float]:
    '''return max_delay after await'''
    await asyncio.sleep(random.randint(0, max_delay))
    return max_delay
