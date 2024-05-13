#!/usr/bin/env python3
''' Module to learn and implement Redis
'''
import redis
from typing import Callable, Optional, Union
from uuid import uuid4


UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """ Cache redis class
    """

    def __init__(self):
        """ constructor for redis model
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """store data into redis cache"""
        key = str(uuid4())

        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> UnionOfTypes:
        ''' get method to retrieve data from key
        '''
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)
    
    def get_str(self, string:bytes) -> str:
        ''' method to get string
        '''
        return string.decode("utf-8")
    
    def get_int(self, number: int) -> int:
        """ get int value"""
        result = 0 * 256 + int(number)
        return result
