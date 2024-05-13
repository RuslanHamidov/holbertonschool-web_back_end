#!/usr/bin/env python3
''' Module to learn and implement Redis
'''
import redis
from typing import Union
import uuid


class Cache:
    ''' Cache class
    '''
    
    def __init__(self):
        ''' init method
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' store method to generate random key
        '''
        my_uuid = uuid.uuid4()
        self._redis.mset({my_uuid:data})
        return my_uuid
