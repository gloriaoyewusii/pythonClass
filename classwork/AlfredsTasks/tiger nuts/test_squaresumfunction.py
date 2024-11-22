from unittest import TestCase
import squaresumfunction

class TestSquareSumFunction(TestCase):
	def test_that_square_sum_function_exists(self):
		squaresumfunction.get_square_sums([1, 2, 3, 4])
	def test_that_square_sum_function_returns_correct_value(self):
		actual = squaresumfunction.get_square_sums([1, 2, 3, 4])
		expected = 30
		self.assertEqual(actual, expected)
	