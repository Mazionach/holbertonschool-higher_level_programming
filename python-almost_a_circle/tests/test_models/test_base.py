#!/usr/bin/python3

"""
Tests for model shapes
"""
from models import base

import unittest

class TestBase(unittest.TestCase):
    
    def test___init__(self):
        self.A = base.Base()
        self.assertEqual(self.A.id, 1)
        self.B = base.Base()
        self.assertEqual(self.B.id, 2)
        self.C = base.Base(16)
        self.assertEqual(self.C.id, 16)
        self.D = base.Base(-10)
        self.assertEqual(self.D.id, -10)


if __name__ == "__main__":
    unittest.main()
