year = int(input("Enter a year: "))
leapYear = year % 4

if leapYear == 0:
	print(f"{year} is a leap year")

if (leapYear != 0):
	print(f"{year} is not a leap year")
