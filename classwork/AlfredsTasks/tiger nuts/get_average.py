def get_average(numbers:list):
	total = 0
	for number in numbers:
		total = total + number
		length = len(numbers)
		average = total/length
	return average

numbers = [10, 20, 30, 40]
print(get_average(numbers))
	