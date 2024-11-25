def getDigitsOf(number):
	while (number > 0):
		remainder = number % 10
		quotient = number / 10
		number = quotient
		
	
	return remainder


number = 67893
print(getDigitsOf(number))