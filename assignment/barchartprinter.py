numberCounter = 1
asteriskCounter = 1

while numberCounter <= 5:
	number = int(input("Enter number: "))
	numberCounter+=1
	
	if number > 1 and number < 30:
		asterisks = ""
		asteriskCounter*=number
		print(asterisks)

	
	