for index in range(1, 100):
	for index2 in range(1, 100):
		integer = index + index2
user_input = int(input(f"What is the sum of {index} + {index2}: "))	
if integer == user_input:
	print(True)
else:
	print(False)