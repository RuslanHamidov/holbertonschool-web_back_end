#!/usr/bin/env python3
''' Testing function with unittest module
'''
import unittest
from utils import access_nested_map, get_json, memoize
import requests
from parameterized import parameterized, parameterized_class
from functools import wraps


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' testing access to map
        '''
        self.assertEqual(access_nested_map((nested_map, path), expected))
