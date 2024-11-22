def get_sum(number:list):
	sum = 0
	even = []
	for counter in number:
		if counter%2 == 0:
			even.append(counter)
			sum += counter
	return sum	
number = [1, 2, 3, 4, 5, 6]
print(get_sum(number))