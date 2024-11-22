def get_sum(numbers:list):
	total = 0
	total2 = 0
	add = []
	new_total = []
	for count in range(0, len(numbers)):
		for counter in numbers:
			add.append(counter)
			total += counter
	for index in numbers:	
		total2 += index
	new_total = total - total2

	return new_total
	

number = (1, 2, 3, 4, 5, 6)
print(get_sum(number))	
		
