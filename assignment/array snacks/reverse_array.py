def reverseArrayOf(numbers):
	reversed_numbers = []		
	for index in range(0, len(numbers)):  
		initial = numbers[index]
		numbers[index] = numbers[len(numbers)-1-index]
		numbers[len(numbers)-1-index] = initial
		reversed_numbers.append(numbers[index])
	return reversed_numbers	
completeNumbers = [3, 4, 5, 6, 7]
print(reverseArrayOf(completeNumbers))