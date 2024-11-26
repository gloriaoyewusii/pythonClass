from unittest import TestCase

import get_even_or_odd

class TestEvenOrOddFunction(TestCase):
	def test_that_even_or_odd_function_exists(self):
		get_even_or_odd.get_even_or_odd(3)
	def test_that_even_or_odd_function_returns_correct_value(self):
		actual = get_even_or_odd.get_even_or_odd(3)
		expected = False
		self.assertEqual(actual, expected)

import prime_number
class TestPrimeNumber(TestCase):
	def test_that_is_prime_function_exists(self):
		prime_number.isPrimeOf(5)
	def test_that_is_prime_function_returns_correct_value(self):
		actual = prime_number.isPrimeOf(5)
		expected = True
		self.assertEqual(actual, expected)

import subtraction
class TestSubtractionFunction(TestCase):
	def test_that_subtract_function_exists(self):
		subtraction.subtract(5, 4)
	def test_that_subtract_function_returns_correct_value(self):
		actual = subtraction.subtract(5, 4)
		expected = 1
		self.assertEqual(actual, expected)

	
import division
class TestDivisionFunction(TestCase):
	def test_that_division_function_exists(self):
		division.divide(6, 3)
	def test_that_division_function_returns_correct_value(self):
		actual = division.divide(10, 2)
		expected = 5
		self.assertEqual(actual, expected)

	
import factors
class TestFactorsFunction(TestCase):
	def test_that_factors_function_exists(self):
		factors.factors(10)
	def test_that_factors_function_returns_correct_value(self):
		actual = factors.factors(10)
		expected = 4
		self.assertEqual(actual, expected)
	



import palindrome
class TestPalindromeFunction(TestCase):
	def test_that_palindrome_function_exists(self):
		palindrome.is_palindrome(45654)
	def test_that_palindrome_function_returns_correct_value(self):
		actual = palindrome.is_palindrome(45254)
		expected = True
		self.assertEqual(actual, expected)

import factorialOf
class TestFactorialFunction(TestCase):
	def test_that_factorial_function_exists(self):
		factorialOf.factorialOf(5)
	def test_that_factorial_function_returns_correct_value(self):
		actual = factorialOf.factorialOf(5)
		expected = 120
		self.assertEqual(actual, expected)

		
import squarefunction
class TestSquareFunction(TestCase):
	def test_that_square_function_exists(self):
		squarefunction.get_square(5)
	def test_that_square_function_returns_correct_value(self):
		actual = squarefunction.get_square(5)
		expected = 25
		self.assertEqual(actual, expected)

		

import square
class TestSquareFunction(TestCase):
	def test_that_square_function_exists(self):
		square.square(10)
	def test_that_square_function_returns_correct_value(self):
		actual = square.square(10)
		expected = False
		self.assertEqual(actual, expected)
	def test_that_square_function_returns_another_correct_value(self):
		actual = square.square(25)
		expected = True
		self.assertEqual(actual, expected)














