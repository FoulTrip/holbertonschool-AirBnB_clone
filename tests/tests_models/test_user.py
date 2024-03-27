#!/usr/bin/python3
"""Unittest for user file: class and methods"""

import pycodestyle
import unittest
from models import user
from models.user import User


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pycodestyle.StyleGuide(quiet=True)
        user_pep8 = "models/user.py"
        test_user_pep8 = "tests/test_user.py"
        result = style.check_files([user_pep8, test_user_pep8])
        self.assertEqual(result.total_errors, 0)


class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(user.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        if User.__doc__ is not None:
            self.assertTrue(len(User.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(User):
            if func.__doc__ is not None:
                self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
