#!/usr/bin/env python3
'''
Description: function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
Arguments: k: string
v : int or float
'''

from typing import Tuple, Union

def to_kv(k:str, v: Union[float, int]) -> Tuple:
    return Tuple[k, v]
    