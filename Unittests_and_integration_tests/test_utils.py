#!/usr/bin/env python3
''' Testing function with unittest module
'''
import unittest
import utils
import requests
from parameterized import parameterized, parameterized_class
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, input, expected):
        ''' testing access to map
        '''
        self.assertEqual(utils.access_nested_map(input, expected))


if __name__ == '__main__':
    unittest.main()
