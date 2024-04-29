#!/usr/bin/env python3
''' Testing function with unittest module
'''
import unittest
import utils
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    def test_access_nested_map(self):
        ''' testing access to map
        '''
        self.assertEqual(utils.access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "b")), 2)


if __name__ == '__main__':
    unittest.main()
