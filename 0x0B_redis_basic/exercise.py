#!/usr/bin/env python3
''' Module to learn and implement Redis
'''
import redis
from typing import Union


class Cache:
    ''' Cache class
    '''
    def __init__(self):
        ''' init method
        '''
        _redis = redis.Redis()
        _redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' store method to generate random key
        '''
        pass
