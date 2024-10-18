x = 2 
y = 3

print('x =', x)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), 'x =', (y + x))

rating = input('Enter an integer rating between 1 and 10: ')
print("rating is", rating)

grade = int(input('Enter a grade: '))
if (grade >= 90):
	print('Congratulations! Your grade of', grade, 'earns you an A in this course\n')

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

radius = int(input("Enter the radius: "))
areaCircle = 3.142 * radius * radius
print('Area of a circle is :', areaCircle)
diameter = 2 * radius
print('Diameter is: ', diameter)
circumference = 2 * 3.142 * radius
print('Circumference is: ', circumference)


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