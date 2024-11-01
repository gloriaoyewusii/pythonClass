result1 = 0
result2 = 0
number = int(input("Number: "))
number2 = int(input("Number 2: "))
while number <= 4**5:
	print(number)
	result1 += number
	number*=4		
print(f"Sum is: {result1}")
print(" ")
while number2 <= 8**5:
	print(number2)
	result2 += number2
	number2*=8
print(f"Sum is: {result2}")

pair_of_result = result1 + result2
print(f"Sum of pair is: {pair_of_result}")
