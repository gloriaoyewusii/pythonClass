from unittest import TestCase
import digitssumfunction

class TestDigitsSumFunction(TestCase):
	def test_that_digits_sum_function_exists(self):
		digitssumfunction.get_digits_sum(12345)
	def test_that_digits_sum_function_returns_correct_value(self):
		actual = digitssumfunction.get_digits_sum(15324)
		expected = 15
		self.assertEqual(actual, expected)
		

	