from unittest import TestCase
import palindromefunction

class TestPalindromeFunction(TestCase):
	def test_that_palindrome_function_exists(self):
		palindromefunction.get_palindrome("madam")
	def test_that_palindrome_function_returns_correct_value(self):
		actual = palindromefunction.get_palindrome("madam")
		expected = True
		self.assertEqual(actual, expected)
		actual = palindromefunction.get_palindrome("oyanowww")
		expected = False
		self.assertEqual(actual, expected)

