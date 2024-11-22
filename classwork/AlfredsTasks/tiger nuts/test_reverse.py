from unittest import TestCase
import reversefunction

class TestReverseFunction(TestCase):
	def test_that_reverse_function_exists(self):
		reversefunction.get_reverse("yamacita")
	def test_that_reverse_function_returns_correct_value(self):
		actual = reversefunction.get_reverse("yamacita")
		expected = "aticamay"
		self.assertEqual(actual, expected)
		actual = reversefunction.get_reverse("ogechi")
		expected = "ihcego"
		self.assertEqual(actual, expected)

	
