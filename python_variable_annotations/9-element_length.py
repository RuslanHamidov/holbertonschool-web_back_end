#!/usr/bin/env python3
'''
Description: function make_multiplier that takes
a float multiplier as argument and returns a
function that multiplies a float by multiplier.
Arguments: multiplier: float
'''

from typing import List, Sequence, Tuple


def element_length(lst: List[int]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
