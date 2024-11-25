def get_even_or_odd(integer):
	integer = int(input("Enter a number: "))
	if integer % 2 == 0:
		return True
	elif integer % 2 != 0:
		return False

integer = 25
print(get_even_or_odd(integer))