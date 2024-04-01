#!/usr/bin/env python3
'''
Auqment function do duct type
Arguments: lst: iterable[sequence]
'''

from typing import Any, Optional 


def safe_first_element(lst: Any) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
