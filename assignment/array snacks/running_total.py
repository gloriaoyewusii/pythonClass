def findRunningTotalIn(numbers):	
	total = 0
	running_total = 0
	for index in range(0, len(numbers)):
		total = numbers[index] + total
		running_total = total + total
	return running_total
		
completeNumbers = [1, 2, 3, 4]
print(findRunningTotalIn(completeNumbers))


