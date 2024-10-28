import random
randomNumber = random.randint(1, 3000000000)
userInput = int(input("Guess random number: "))
if userInput > randomNumber:
	print("Too high, try again")
else: 
	if userInput < randomNumber:
		print("Too low, try again")
	else:
		if userInput == randomNumber:
			print("Correct!")
