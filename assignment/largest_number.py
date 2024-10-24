numberCounter = 1
number = int(input("Enter a number: "))
largest_number = number
smallest_number = number
user_Input = 1		
while numberCounter <= 4:

	number = int(input("Enter a number: "))
	numberCounter+=1

	if number > largest_number:
		largest_number = number

	elif number < smallest_number:
		smallest_number = number

if user_Input == 0:	
	print("Calculation terminated")

user_Input = int(input("Enter 0 if you want to stop: "))

		

print("smallest number is: ", smallest_number)
print("largest number is: ", largest_number)


