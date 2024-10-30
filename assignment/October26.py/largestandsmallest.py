number = int(input("Enter a number to start or -1 to quit: "))
largestNumber = number
smallestNumber = number
	
while number != -1:	
	number = int(input("Enter a number to start or -1 to quit: "))
	if number != -1 and number > largestNumber:
		largestNumber = number
	else:
		if number != -1 and number < smallestNumber:
			smallestNumber = number
	
	print(f"The largest number is: {largestNumber}")
	print(f"The smallest number is: {smallestNumber}")