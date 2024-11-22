def get_average(numbers:list):
	total = 0
	for number in numbers:
		total = total + number
		length = len(numbers)
		average = total/length
	return average

