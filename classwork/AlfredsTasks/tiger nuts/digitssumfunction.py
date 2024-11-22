def get_digits_sum(number):
	total = 0
	for index in str(number):	
		total += int(index)
	return total

number = 15324
print(get_digits_sum(number))