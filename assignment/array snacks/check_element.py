def checkElementIn(numbers):
	elementToCheck = int(input("Enter element to check: "))
	for index in range(0, len(numbers)): 
		if elementToCheck == numbers[index]:
			print(elementToCheck, " is in the list.")
		
	return numbers
completeNumbers = [3, 4, 5, 6, 7]
print(checkElementIn(completeNumbers))