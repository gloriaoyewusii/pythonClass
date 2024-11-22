from unittest import TestCase
import mergefunction

class TestMergeFunction(TestCase):
	def test_that_merge_function_exists(self):
		mergefunction.get_merger([1, 2, 3, 4], [56, 7, 34, 9])
	def test_that_merge_function_returns_correct_value(self):
		actual = mergefunction.get_merger([1, 2, 3, 4,-8], [56, 7, 34, 9,99])
		expected = [-8,1, 2, 3, 4, 7, 9, 34, 56,99]
		self.assertEqual(actual, expected)
	
