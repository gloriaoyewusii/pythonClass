"""
Prompt the user to enter a number.
Collect and store as first_number, second_number and third_number.
if first_number is greater than second_number and second_number is greater third_number, display the numbers in ascending order

if second_number is greater than first_number and first_number is greater than third_number, display the numbers in ascending order

if third_number is greater than first_number and first_number is greater than second_number, display the numbers in ascending order
"""


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number > second_number and second_number > third_number:
	print(f"{third_number}, {second_number}, {first_number}")
elif second_number > first_number and first_number > third_number:
	print(f"{third_number}, {first_number}, {second_number}")
elif third_number > first_number and first_number > second_number:
	print(f"{second_number}, {first_number}, {third_number}")
elif first_number < second_number and second_number < third_number:
	print(f"{first_number}, {second_number}, {third_number}")
elif first_number > second_number and second_number < third_number:
	print(f"{second_number}, {third_number}, {first_number}")


