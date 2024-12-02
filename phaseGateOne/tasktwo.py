"""
prompt the user to enter a number.
collect and store as number.
ensure the number is between number 1 and 1000
create another variable called sum_of_digits.
initialise to 0
if number meets selection condition expression, calculate the sum of the digits.
cast the number variable using the string to make it iterable.
loop through the numbers using a varible identified as index.
when calculating the sum, cast the index to be of int format
display the sum in the sum_of_digits variable.
"""

number = int(input("Enter a number between 1 and 1000: "))

sum_of_digits = 0

if number > 999 or number < 0:
		number = int(input("Enter a number between 1 and 1000: "))
else: 	
	number = str(number)
	for index in number:
		sum_of_digits += int(index)
	print(f"Sum of digts = {sum_of_digits}")
	



