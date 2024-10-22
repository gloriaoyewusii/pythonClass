baseNumber = int(input("Base number: "))
exponentNumber = int(input("Exponent number: "))

iteration_number = 1 
result = 1
new_result = 0
while iteration_number <= exponentNumber:
	result*=baseNumber
	iteration_number+=1 
	new_result = result

	if iteration_number > exponentNumber:
		break
print(baseNumber, "raised to the power of", exponentNumber, "is: ", result)

	
	

