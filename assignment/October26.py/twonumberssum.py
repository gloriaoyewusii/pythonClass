number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
	
total = 0
total = number1 + number2;
print(f"Total is: {total}")
sentinel = -1
	
userConfirmation = int(input("Enter -1 to quit operation, otherwise enter a different number to continue: "))
	
while userConfirmation != sentinel:
	if userConfirmation == -1:
    		print("Operation terminated")
	else:
		number1 = int(input("Enter first number: "))
		number2 = int(input("Enter second number: "))
		total = number1 + number2
	print(f"Total is: {total}")

	userConfirmation = int(input("Enter -1 to quit operation, otherwise enter a different number to continue: "))

