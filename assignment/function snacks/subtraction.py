def subtract(number1, number2):
	if number1 > number2:
		subtraction = number1 - number2
	elif number1 < number2:
		subtraction = number2 - number1
	return subtraction

number1 = 20
number2 = 5

print(subtract(number1, number2))