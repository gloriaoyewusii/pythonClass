from unittest import TestCase
import commonelementfunction

class TestCommonElementFunction(TestCase):
	def test_that_common_element_function_exists(self):
		commonelementfunction.get_common_element([1, 3, 5], [2, 3, 4])
	def test_that_common_element_function_returns_correct_value(self):
		actual = commonelementfunction.get_common_element([1, 3, 5], [2, 3, 4])
		expected = 3
		self.assertEqual(actual, expected)
	def test_that_common_element_function_returns_correct_value(self):
		actual = commonelementfunction.get_common_element([2, 3, 5], [2, 8, 4])
		expected = 2
		self.assertEqual(actual, expected)