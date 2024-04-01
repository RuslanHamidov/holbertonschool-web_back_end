#!/usr/bin/env python3
'''
Description: function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
Arguments: k: string
v : int or float
'''

from typing import Tuple, Union


def to_kv(k:str, v: Union[float, int]) -> Tuple[str, float]:
    '''return tuple of str and float power 2'''
    return k, v**2
