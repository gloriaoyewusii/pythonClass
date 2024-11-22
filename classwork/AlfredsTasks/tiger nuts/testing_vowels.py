from unittest import TestCase
import vowelsfunction

class TestVowelsFunction(TestCase):
	def test_that_vowels_function_exists(self):
		vowelsfunction.get_vowels("python is sweet")
	def test_that_vowelfunction_function_returns_correct_value(self):
		actual = vowelsfunction.get_vowels("Jesus is Lord")
		expected = 4
		self.assertEqual(actual, expected)
	def test_that_vowelfunction_function_returns_correct_value(self):
		actual = vowelsfunction.get_vowels("python is sweet")
		expected = 4
		self.assertEqual(actual, expected)




	
