from unittest import TestCase
import primefunction

class TestPrimeFunction(TestCase):
	def test_that_prime_function_exists(self):
		primefunction.get_prime(29)
	def test_that_prime_function_returns_correct_value(self):
		actual = primefunction.get_prime(37)
		expected = True
		self.assertEqual(actual, expected)

	
