#!/usr/bin/env python3
""" function measures wait_n execution time """
import asyncio
import time
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    task1 = asyncio.create_task(wait_random(max_delay))
    return task1
