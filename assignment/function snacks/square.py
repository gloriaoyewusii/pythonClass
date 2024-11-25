def square(integer):
	squareCounter = 0
	for index in range(1, integer):
		if index * index == integer:
			squareCounter += 1;
		if squareCounter == 1:
			return True
		else:
			return False


integer = 10;
print(square(integer))
	