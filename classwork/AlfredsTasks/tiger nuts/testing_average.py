from unittest import TestCase
import averagefunction

class TestAverageFunction(TestCase):
	def test_that_average_function_exists(self):
		averagefunction.get_average([2, 4, 6])
	def test_that_vowelfunction_function_returns_correct_value(self):
		actual = averagefunction.get_average([10, 20, 30])
		expected = 20
		self.assertEqual(actual, expected)

	
