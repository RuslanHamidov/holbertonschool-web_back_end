#!/usr/bin/env python3
'''
Description: function make_multiplier that takes
a float multiplier as argument and returns a
function that multiplies a float by multiplier.
Arguments: multiplier: float
'''

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns tuple in list'''
    return [(i, len(i)) for i in lst]
