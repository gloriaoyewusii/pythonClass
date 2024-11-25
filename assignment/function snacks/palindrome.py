def is_palindrome(integer):
	lastDigit = integer % 10
	fourthDigit = (integer/10) % 10

	secondDigit = (integer / 1000) % 10
	firstDigit = (integer/10000) % 10

	if lastDigit == firstDigit and secondDigit == fourthDigit:
		return True
	elif lastDigit != firstDigit and secondDigit != fourthDigit:

		return False

integer = 45654;
print(is_palindrome(integer))

