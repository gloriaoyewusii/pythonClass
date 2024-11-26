from unittest import TestCase

import concatenate_lists

class TestConcatenateFunction(TestCase):
	def test_that_concatenate_lists_function_exists(self):
		concatenate_lists.concatenate_lists(['a', 'b', 'c'], [1, 2, 3])
	def test_that_concatenate_lists_function_returns_correct_value(self):
		actual = concatenate_lists.concatenate_lists(['a', 'b', 'c'], [1, 2, 3])
		expected = ['a', 'b', 'c', 1, 2, 3]
		self.assertEqual(actual, expected)
	
import running_total
class TestRunningTotalFunction(TestCase):
	def test_that_running_total_function_exists(self):
		running_total.findRunningTotalIn([1, 2, 3, 4])
	def test_that_running_total_function_returns_correct_value(self):
		actual = running_total.findRunningTotalIn([1, 2, 3, 4])
		expected = 20
		self.assertEqual(actual, expected)


import odd_elements
class TestOddElementsFunction(TestCase):
	def test_that_odd_elements_function_exists(self):
		odd_elements.printOddElementsIn([3, 4, 5, 6, 7])
	def test_that_odd_elements_function_returns_correct_value(self):
		actual = odd_elements.printOddElementsIn([3, 4, 5, 6, 7])
		expected = [3, 5, 7]
		self.assertEqual(actual, expected)


		
import even_elements
class TestEvenElementsFunction(TestCase):
	def test_that_even_elements_function_exists(self):
		even_elements.printEvenElementsIn([3, 4, 5, 6, 7])
	def test_that_even_elements_function_returns_correct_value(self):
		actual = even_elements.printEvenElementsIn([3, 4, 5, 6, 7])
		expected = [4, 6]
		self.assertEqual(actual, expected)


import largestfunction
class TestEvenElementsFunction(TestCase):
	def test_that_largest_function_exists(self):
		largestfunction.get_largest([3, 4, 9, 6, 7])
	def test_that_largest_function_returns_correct_value(self):
		actual = largestfunction.get_largest([3, 4, 9, 6, 7])
		expected = 9
		self.assertEqual(actual, expected)


import list_total
class TestListFunction(TestCase):
	def test_that_list_total_function_exists(self):
		list_total.first_sum(1234)
	def test_that_list_total_function_returns_correct_value(self):
		actual = list_total.first_sum(1234)
		expected = 10
		self.assertEqual(actual, expected)


import check_element
class TestCheckElementsFunction(TestCase):
	def test_that_check_elements_function_exists(self):
		check_element.checkElementIn([3, 4, 5, 6, 7])
	def test_that_check_elements_function_returns_correct_value(self):
		actual = check_element.checkElementIn([3, 4, 5, 6, 7])
		expected = [3, 5, 7]
		self.assertEqual(actual, expected)
		

import reverse_array
class TestReverseArrayFunction(TestCase):
	def test_that_reverse_array_function_exists(self):
		reverse_array.reverseArrayOf([3, 4, 5, 6, 7])
	def test_that_reverse_array_function_returns_correct_value(self):
		actual = reverse_array.reverseArrayOf([3, 4, 5, 6, 7])
		expected = [7, 6, 5, 4, 3]
		self.assertEqual(actual, expected)

		

		
