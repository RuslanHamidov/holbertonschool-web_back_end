#!/usr/bin/env python3
''' Description: asynchronous coroutine that takes in an integer argument
                 (max_delay, with a default value of 10) named wait_random
                 that waits for a random delay between 0 and max_delay
                 (included and float value) seconds and eventually returns it
    Arguments: max_delay: int = 10
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
    for i in range(n - 1) :
        flag = 0
        for j in range(n - 1) :
            if await_list[j] > await_list[j + 1] :
                tmp = await_list[j]
                await_list[j] = await_list[j + 1]
                await_list[j + 1] = tmp
                flag = 1

        if flag == 0:
            break
        
    return await_list
