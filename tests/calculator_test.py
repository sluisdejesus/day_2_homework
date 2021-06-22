import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    pass                                

    def test_add(self):
        self.assertEqual(5,add(2,3))

    def test_subtract(self):
        self.assertEqual(7,subtract(10,3))

    def test_multiply(self):
        self.assertEqual(20,multiply(5,4))

    def test_divide(self):
        self.assertEqual(10,divide(50,5))