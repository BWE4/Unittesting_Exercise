import unittest
from even_odd_function import even_numbers_to_nth
from even_odd_function import odd_numbers_to_nth
class TestNumberFunctions(unittest.TestCase):
    
    def test_even_numbers_to_nth(self):
        self.assertEqual(even_numbers_to_nth([1, 2, 3, 4, 5, 6], 6), "2 4 6")
        self.assertEqual(even_numbers_to_nth([10, 15, 20, 25, 30], 4), "10 20")
        self.assertEqual(even_numbers_to_nth([1, 3, 5, 7], 4), "")
        self.assertEqual(even_numbers_to_nth([], 3), "")
        self.assertEqual(even_numbers_to_nth([2, 4, 6], 2), "2 4")
    
    def test_odd_numbers_to_nth(self):
        self.assertEqual(odd_numbers_to_nth([1, 2, 3, 4, 5, 6], 6), "1 3 5")
        self.assertEqual(odd_numbers_to_nth([10, 15, 20, 25, 30], 4), "15 25")
        self.assertEqual(odd_numbers_to_nth([2, 4, 6, 8], 4), "")
        self.assertEqual(odd_numbers_to_nth([], 3), "")
        self.assertEqual(odd_numbers_to_nth([1, 3, 5], 2), "1 3")

if __name__ == "__main__":
    unittest.main()
