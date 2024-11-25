def factorialOf(integer):
	factorial = integer;
	for index in range(1, integer):
		factorial *= integer - index;
		
	return factorial

integer = 5
print(factorialOf(integer))