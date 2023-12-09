import unittest
from app import function1

class TestFunctions(unittest.TestCase):

    def test_function1_returns_none(self):
        result = function1()
        self.assertIsNone(result, "function1 should return None")

if __name__ == '__main__':
    unittest.main()

