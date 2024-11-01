firstNumber = int(input("First number: "))
secondNumber = int(input("Second number: "))
thirdNumber = int(input("Third number: "))

if thirdNumber > firstNumber and firstNumber < secondNumber:
	print("Numbers are in ascending order")
if firstNumber > secondNumber and secondNumber > thirdNumber:
	print("Numbers are in descending order")
if secondNumber < firstNumber and firstNumber > thirdNumber:
	print("Numbers are neither in ascending nor descending order")
