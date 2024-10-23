number1 = int(input("Enter an integer: "))
print(number1)
number2 = int(input("Enter an integer: "))
print(number2)
number3 = int(input("Enter an integer: "))
print(number3)

sum = number1 + number2 + number3
print("Sum: ", sum)
average = sum/3
print("Average: ",average)
product = number1 * number2 * number3
print("Product: ", product)

if (number1 < number2 and number3):
	print("smallest number is:", number1)
elif (number2 < number1 and number3):
	print("smallest number is:", number2)
elif (number3 < number1 and number2):
	print("smallest number is:", number3)

if (number1 > number2 and number3):
	print("largest number is:", number1)
if (number2 > number1 and number3):
	print("largest number is:", number2)
if (number3 > number1 and number2):
	print("largest number is:", number3)

