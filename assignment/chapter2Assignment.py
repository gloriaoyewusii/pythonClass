print((2.1))
x = 2 
y = 3

print('x =', x)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), 'x =', (y + x))


print((2.2))
rating = input('Enter an integer rating between 1 and 10: ')
print("rating is", rating)


print((2.3))
grade = int(input('Enter a grade: '))
if (grade >= 90):
	print('Congratulations! Your grade of', grade, 'earns you an A in this course\n')



print((2.4))
value1 = 27.5 + 2
print('value1 is: ', value1)
value2 = 27.5 - 2
print('value2 is: ', value2)
value3 = 27.5 * 2
print('value3 is: ', value3)
value4 = 27.5 / 2
print('value4 is: ', value4)
value5 = 27.5 // 2
print('value5 is: ', value5)
value6 = 27.5 ** 2
print('value6 is: ', value6)

print((2.5))
radius = int(input("Enter the radius: "))
areaCircle = 3.142 * radius * radius
print('Area of a circle is :', areaCircle)
diameter = 2 * radius
print('Diameter is: ', diameter)
circumference = 2 * 3.142 * radius
print('Circumference is: ', circumference)



print((2.6))
number = int(input("Enter a three digit number: "))
last_number = number % 10
test_number = number // 10
second_number = test_number % 10
first_number = test_number // 10
print("The inverse number is: ", last_number, second_number, first_number)

odd_numbers = 0
even_numbers = 0

if (last_number % 2 != 0):
	odd_numbers+=1
if (second_number % 2 != 0):
	odd_numbers+=1
if (first_number % 2 != 0):
	odd_numbers+=1
if (last_number % 2 == 0):
	even_numbers+=1
if (second_number % 2 == 0):
	even_numbers+=1
if (first_number % 2 == 0):
	even_numbers+=1
print("Odd number is: ", odd_numbers)
print("Even number is: ", even_numbers)



print((2.7))
num1 = 1024
if (num1 % 4 == 0):
	print("num1 is a multiple of 4")
if (num1 % 4 != 0):
	print("num1 is not a multiple of 4")
num2 = 2
if (num2 % 10 == 0):
	print("num2 is a multiple of 10")
if (num2 % 10 != 0):
	print("num2 is not a multiple of 10")


print((2.8))
print("number\tsquare\tcube")
print('0\t0\t0\n1\t1\t1\n2\t4\t8\n3\t9\t27\n4\t16\t64\n5\t25\t125\n\n')

print((2.9))
print(ord('B')) 
print(ord('C'))
print(ord('D')) 
print(ord('b'))
print(ord('c')) 
print(ord('d'))
print(ord('0')) 
print(ord('1'))
print(ord('$')) 
print(ord('*'))
print(ord('+')) 
print(ord(' '))

print((2.10))
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


print((2.11)

number = int(input("Enter number: "))
fifth_number = number % 10
int_number1 = number // 10
fourth_number = int_number1 % 10
int_number2 = int_number1 // 10
third_number = int_number2 % 10
int_number3 = int_number2 // 10
second_number = int_number3 % 10
first_number = int_number3 // 10

print("The digits are: ", end=", ", first_number, second_number, third_number, fourth_number, fifth_number, end="   ")


print((2.12))
principal = float(input("Original amount invested: "))
annual_rate = float(input("Annual rate of return: "))
numberOfYears = float(input("Number of years: "))
rate = annual_rate/100

amount_deposit = (principal) * ((1 + rate) ** numberOfYears)
print(f"Amount deposited is {amount_deposit:.2f}")

print((2.13))

users_age = int(input("Age: "))
maximumHeartRate = int(input("220 - users_age"))
for targetHeartRate in range(50, 85)