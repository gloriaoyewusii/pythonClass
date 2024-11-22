from unittest import TestCase
import anagramfunction

class TestAnagramFunction(TestCase):
	def test_that_anagram_function_exists(self):
		anagramfunction.get_anagram("silent", "listen")
	def test_that_anagram_function_returns_correct_value(self):
		actual = anagramfunction.get_anagram("silent", "listen")
		expected = True
		self.assertEqual(actual, expected)
		actual = anagramfunction.get_anagram("baba", "abba")
		expected = True
		self.assertEqual(actual, expected)

		


	
