def get_odd_digits_sum(number):
	total = 0
	number = str(number)
	for index in number:
		
		if int(index) % 2 != 0:	
			total += int(index)
	return total

number = 12345
print(get_odd_digits_sum(number))