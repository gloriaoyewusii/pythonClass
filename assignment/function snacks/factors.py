def factors(integer):
	factors = 1
	for index in range(1, integer):
		if integer % index == 0:
			factors += 1
	return factors
	
integer = 10
print(factors(integer))