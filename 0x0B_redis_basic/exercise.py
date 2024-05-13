#!/usr/bin/env python3
''' Module to learn and implement Redis
'''
import redis
from typing import Union
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
