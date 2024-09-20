import unittest
from solve import addition

class TestAdditionFunction(unittest.TestCase):

    # Test: One of the arguments being zero
    def test_addition_with_zero(self):
        self.assertEqual(addition('0', '123', 10), '123', "Failed when x is 0")
        self.assertEqual(addition('123', '0', 10), '123', "Failed when y is 0")

    # Test: Both x and y positive
    def test_addition_both_positive(self):
        self.assertEqual(addition('A3F', '1B2', 16), 'BF1', "Failed when both x and y are positive in base 16")
        self.assertEqual(addition('123', '456', 10), '579', "Failed when both x and y are positive in base 10")
        self.assertEqual(addition('101', '110', 2), '1011', "Failed when both x and y are positive in base 2")

    # Test: Both x and y negative
    def test_addition_both_negative(self):
        self.assertEqual(addition('-FF', '-1A', 16), '-119', "Failed when both x and y are negative in base 16")
        self.assertEqual(addition('-321', '-654', 10), '-975', "Failed when both x and y are negative in base 10")
        self.assertEqual(addition('-1101', '-101', 2), '-10010', "Failed when both x and y are negative in base 2")

if __name__ == '__main__':
    unittest.main()