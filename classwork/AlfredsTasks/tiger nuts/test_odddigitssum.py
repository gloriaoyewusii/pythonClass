from unittest import TestCase
import odddigitsfunction

class TestOddDigitsSumFunction(TestCase):
	def test_that_odd_digits_function_exists(self):
		odddigitsfunction.get_odd_digits_sum(12345)
	def test_that_odd_digits_function_returns_correct_value(self):
		actual = odddigitsfunction.get_odd_digits_sum(12345)
		expected = 9
		self.assertEqual(actual, expected)