#!/usr/bin/env python3
'''
Description: Import wait_random from the previous python file that
you’ve written and write an async routine called wait_n
that takes in 2 int arguments: max_delay and n. You will
spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays(float values)
The list of the delays should be in ascending order without
using sort() because of concurrency.
Arguments: n: int, max_delay: int = 10
'''

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''returns list of awaits'''
    await_list: List[float] = []
    for i in range(n):
        await_list.append(await wait_random(max_delay))
    return sort_list(await_list)

def sort_list(await_list: List[float]) -> List[float]:
    '''sorts list of awaits'''
    n = len(await_list)
    for i in range(n - 1):
        flag = 0
        for j in range(n - 1):
            if await_list[j] > await_list[j + 1]:
                tmp = await_list[j]
                await_list[j] = await_list[j + 1]
                await_list[j + 1] = tmp
                flag = 1
        if flag == 0:
            break
    return await_list
