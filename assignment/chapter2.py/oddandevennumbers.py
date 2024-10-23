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

