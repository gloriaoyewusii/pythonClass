from unittest import TestCase
import mergedfunction

class TestMergedListFunction(TestCase):
	def test_that_merged_list_function_exists(self):
		mergedfunction.get_merged_list([1, 3, 5], [2, 4, 6])
	def test_that_merged_list_function_returns_correct_value(self):
		actual = mergedfunction.get_merged_list([1, 3, 5], [2, 4, 6])
		expected = [1, 2, 3, 4, 5, 6]
		self.assertEqual(actual, expected)
		actual = mergedfunction.get_merged_list([-2, 1, 3, 5, -8], [2, 4, 6, 0, 1.5])
		expected = [-8, -2, 0, 1, 1.5, 2, 3, 4, 5, 6]
		self.assertEqual(actual, expected)