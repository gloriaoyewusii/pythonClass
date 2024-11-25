def first_sum(numbers):
	total = 0
	for index in range(0, len(numbers)):
		total = numbers[index] + total
		index+=1
			
	return total

	def secondSetToSum(numbers):
		total = 0;
		index = 0; 
		while index < len(numbers):
			total = numbers[index] + total
			index+=1
		return total


numbers = 1234
print(first_sum(numbers))