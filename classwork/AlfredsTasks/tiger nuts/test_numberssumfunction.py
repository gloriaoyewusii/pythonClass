from unittest import TestCase
import numberssumfunction

class TestNumbersSumFunction(TestCase):
	def test_that_numbers_sum_function_exists(self):
		numberssumfunction.get_sum([1, 2, 3, 4])
	def test_that_numbers_sum_function_returns_correct_value(self):
		actual = numberssumfunction.get_sum([1, 2, 3, 4])
		expected = 30
		self.assertEqual(actual, expected)
		actual = numberssumfunction.get_sum([1, 2, 3, 4, 5])
		expected = 60
		self.assertEqual(actual, expected)
		actual = numberssumfunction.get_sum([1, 2, 3 ])
		expected = 12
		self.assertEqual(actual, expected)
		print(expected)
		


