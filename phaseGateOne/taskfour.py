import random
subtraction = 0
for number1 in range(1, 10):
	for number2 in range(1, 10):
		user_input = int(input(f"What is the difference between {random.randrange(number2)} - {random.randrange(number1)}: "))
	subtraction = random.randrange(number2) - random.randrange(number1)
	if user_input == subtraction:
		print("Correct!")	
	"""	
	print(f"{random.randrange(number1)} - {random.randrange(number2)} = {subtraction}")
	"""



"""
elif random.randrange(number1) < random.randrange(number2):
			subtraction = random.randrange(number2) - random.randrange(number1)


"""