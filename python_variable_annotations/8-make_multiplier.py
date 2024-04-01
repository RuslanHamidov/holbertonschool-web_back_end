#!/usr/bin/env python3
'''
Description: function make_multiplier that takes
a float multiplier as argument and returns a
function that multiplies a float by multiplier.
Arguments: multiplier: float
'''


def make_multiplier(multiplier: float) -> callable:
    '''returns function'''
    def inner():
        multiplier * multiplier
    return inner
