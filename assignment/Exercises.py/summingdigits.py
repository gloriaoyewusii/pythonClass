aNumber = int(input("Enter integer: "))
rem1 = aNumber % 10
quot1 = aNumber // 10
rem2 = quot1 % 10
quot2 = quot1 // 10


if aNumber > 99:
	sum1 = rem1 + rem2 + quot2
	print(f"The sum of the digits is: {sum1}")
	print(f"The number is: {quot2, rem2, rem1}")

elif aNumber < 99:
	sum2 = rem1 + quot1
	print(f"The sum of the digits is: {sum2}")
	print(f"The number is: {quot1, rem1}")
