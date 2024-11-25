def printEvenElementsIn(numbers):
	for index in range(0, len(numbers)): 
		if numbers[index] % 2 == 0:
			print(numbers[index])
	return numbers[index]
		
completeNumbers = [3, 4, 5, 6, 7]
printEvenElementsIn(completeNumbers)