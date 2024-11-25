def get_largest(numbers:list):
	numbers = []
	count = 0
	for number in numbers:
		entry = int(input("Enter an element: "))
		numbers.extend(entry)
		largest = numbers[0]	
		if numbers[count] > largest:
			largest = numbers[count]
	return largest

numbers = [3, 4, 6, 7, 9]
print(get_largest(numbers))