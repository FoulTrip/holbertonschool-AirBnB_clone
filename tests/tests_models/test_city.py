#!/usr/bin/python3
"""Unittest for test file: class and methods"""

import pycodestyle
import unittest
from models import city
from models.city import City


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pycodestyle.StyleGuide(quiet=True)
        city_pep8 = "models/city.py"
        test_city_pep8 = "tests/test_city.py"
        result = style.check_files([city_pep8, test_city_pep8])
        self.assertEqual(result.total_errors, 0)


class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        if city.__doc__ is not None:
            self.assertTrue(len(city.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        if City.__doc__ is not None:
            self.assertTrue(len(City.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(City):
            if func.__doc__ is not None:
                self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
