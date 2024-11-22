def get_merger(firstArray, secondArray:list):
	firstArray.extend(secondArray)
	firstArray.sort()
	return firstArray

firstArray = [3, 4, 9, 10]
secondArray = [1, 5, 7, 8]
print(get_merger(firstArray, secondArray))
