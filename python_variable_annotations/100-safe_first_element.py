#!/usr/bin/env python3
'''
Auqment function do duct type
Arguments: lst: iterable[sequence]
'''

from typing import Any, Sequence, Optional 


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
