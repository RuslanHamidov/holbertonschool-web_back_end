#!/usr/bin/env python3
''' Testing function with unittest module
'''
import json
import unittest
from utils import access_nested_map, get_json, memoize
import requests
from unittest.mock import patch
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
            access_nested_map(nested_map, path)

        self.assertEqual(
            f'KeyError({str(error.exception)})', repr(error.exception))


class TestGetJson(unittest.TestCase):
    ''' Class to test getJson method from Utils
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        ''' test get_json method
        '''
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    ''' Class to test memoize method
    '''
    
    def test_memoize(self):
        ''' test_memoize method
        '''
        class TestClass:
            ''' Tested Class
            '''
            def a_method(self):
                ''' a_method to return value
                '''
                return 42

            @memoize
            def a_property(self):
                ''' returns a_method
                '''
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_a_method.assert_called_once()
