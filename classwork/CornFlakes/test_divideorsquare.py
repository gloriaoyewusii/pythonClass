from unittest import TestCase

import divideorsquare

class TestDivideOrSquareFunction(TestCase):
	def test_that_divide_or_square_function_exists(self):
		divideorsquare.get_divide_or_square(30)
	def test_that_divide_or_square_function_returns_correct_value(self):
		actual = divideorsquare.get_divide_or_square(20)
		expected = 2
		self.assertEqual(actual, expected)
	def test_that_divide_or_square_returns_rounded_float_values(self):
		actual = divideorsquare.get_divide_or_square(60)
		expected = 3.464
		self.assertEqual(actual, expected)	
		actual = divideorsquare.get_divide_or_square(25)
		expected = 2.236
		self.assertEqual(actual, expected)
	def test_that_divide_or_square_function_inputs_float_value(self):
		actual = divideorsquare.get_divide_or_square(60.5)
		expected = 0.5
		self.assertEqual(actual, expected)
	
	


	
