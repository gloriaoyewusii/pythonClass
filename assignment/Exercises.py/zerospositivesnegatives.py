zeroInputs = 0
negativeInputs = 0
positiveInputs = 0	
numberCounter = 1

while numberCounter <= 5:
	number = int(input("Enter number: "))
	numberCounter+=1
	
	
	if number > 0:
		positiveInputs+=1
	elif number < 0:
		negativeInputs+=1
	else:
		zeroInputs+=1

print(positiveInputs)
print(negativeInputs)
print(zeroInputs)
	
	
