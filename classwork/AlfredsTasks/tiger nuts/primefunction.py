def get_prime(number):
	if number%2 == 0:
		return False
	else:
		for value in range(3, number, 1):
			if number%value==0:
				return False
			else:
				return True