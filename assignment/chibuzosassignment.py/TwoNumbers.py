number1 = int(input("First number: "))
number2 = int(input("Second number: "))
sum = number1 + number2
print("Sum is: ", sum)

user_confirmation = int(input('Enter grade, 0 to end: '))
while user_confirmation != 0:
	number1 = int(input("First number: "))
	number2 = int(input("Second number: "))
	sum = number1 + number2
	print("Sum is: ", sum)
	
	user_confirmation +=1
	user_confirmation = int(input('Enter grade, 0 to end: '))

	if user_confirmation == 0:
		print(user_confirmation)
		print('Calculation terminated')
		



