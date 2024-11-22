def get_square_sums(numbers:list):
	square_sum = 0
	for count in range(0, len(numbers)):
		for element in numbers:
			square = element**2
			square_sum += square
		return square_sum

number = [1, 2, 3, 4]
print(get_square_sums(number))