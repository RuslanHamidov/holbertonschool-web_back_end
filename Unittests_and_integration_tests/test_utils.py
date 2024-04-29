#!/usr/bin/env python3
''' Testing function with unittest module
'''
import unittest
from utils import access_nested_map, get_json, memoize
import requests
from parameterized import parameterized, parameterized_class
from functools import wraps


class TestAccessNestedMap(unittest.TestCase):
    '''Testing access method to check path of nested map
    '''
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' testing access to map
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' testing KeyError
        '''
        with self.assertRaises(KeyError) as error:
            self.test_access_nested_map(nested_map, path)
