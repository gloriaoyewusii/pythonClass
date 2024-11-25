def division(number1, number2):
	if number1 > number2:
		quotient = number1 / number2
	elif number1 < number2:
		quotient = number2 / number1

	elif number1 == 0 or number2 == 0:
		quotient = 0

	return quotient

number1 = 10
number2 = 25
print(division(number1, number2))