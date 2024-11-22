from unittest import TestCase
import acronymfunction

class TestAcronymFunction(TestCase):
	def test_that_acronym_function_exists(self):
		acronymfunction.get_acronym("Pay Later")
	def test_that_acronym_function_returns_correct_value(self):
		actual = acronymfunction.get_acronym("Portable Network Graphics")
		expected = "PNG"
		self.assertEqual(actual, expected)

	
	