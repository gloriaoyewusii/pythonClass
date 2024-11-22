from unittest import TestCase
import removespacefunction

class TestRemoveSpaceFunction(TestCase):
	def test_that_remove_space_function_exists(self):
		removespacefunction.get_space("Hello world!")
	def test_that_remove_space_function_returns_correct_value(self):
		actual = removespacefunction.get_space("Hello world! ")
		expected = "Helloworld!"
		self.assertEqual(actual, expected)
		actual = removespacefunction.get_space("With all my heart")
		expected = "Withallmyheart"
		self.assertEqual(actual, expected)

	

	
