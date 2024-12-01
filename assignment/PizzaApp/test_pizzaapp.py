from unittest import TestCase

import pizzaapp

class TestPizzaAppFunction(TestCase):
	def test_that_pizza_app_function_exists(self):
		pizzaapp.getPizzaFor(12)
	def test_that_pizza_app_function_returns_correct_value(self):
		actual = pizzaapp.getPizzaFor(45)
		expected = 20800
		self.assertEqual(actual, expected)
