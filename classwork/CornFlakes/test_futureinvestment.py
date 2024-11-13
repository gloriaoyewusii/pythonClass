from unittest import TestCase
import futureinvestmentfunction

class TestInvestmentFunction(TestCase):
	def test_that_investment_function_exists(self):
		futureinvestmentfunction.get_investment(5, 9, 10) 
	def_test_that_investment_function_returns_correct_value(self):
		actual = futureinvestmentfunction.get_investment(1000, 5, 10)
		expected = 0.0001
		self.assertEqual(actual, expected)


