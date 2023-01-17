#!/usr/bin/python3
"""Module to test Project Classes"""
import unittest
import pep8

from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """testing Rectangle class"""

    def test_rectangle_instance_base(self):
        """Is new instance an instance of base"""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_string_argument(self):
        """Test exception one arg is string"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_one_arg(self):
        """Test exception one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_no_args(self):
        """Test exception raised when no arg provided"""
        with self.assertRaises(TypeError):
            Rectangle()
            
