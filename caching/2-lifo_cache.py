#!/usr/bin/env python3
'''
class FIFOCache that inherits from BaseCaching and is a caching system
'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Fifo cache class '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''puts item to key element'''
        if key and item:
            if self.cache_data.__len__ + 1 > BaseCaching.MAX_ITEMS:
                last = self.cache_data.popitem()
                print("DISCARD:", last[0])
            self.cache_data[key] = item

    def get(self, key):
        '''get key from cache_data'''
        if key in self.cache_data:
            return self.cache_data[key]
