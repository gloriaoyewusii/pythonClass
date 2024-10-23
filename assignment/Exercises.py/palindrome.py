integer = int(input("Integer is: "))

leftInt = integer % 10
print(f"Last number: {leftInt}")
quotient = integer// 10
midInt = quotient % 10
print(f"Middle number: {midInt}")
rightInt = quotient// 10
print(f"The first number: {rightInt}")

if leftInt == rightInt:
	print(f"Integer {integer} is a palindrome")

elif leftInt != rightInt:
	print(f"Integer {integer} is not a palindrome")

