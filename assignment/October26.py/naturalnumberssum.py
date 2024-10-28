total = 0
counter = 1
naturalNumber = 1


while counter <= 10 and naturalNumber <= 10:
	naturalNumber = int(input(f"Number {counter}: "))
	total = naturalNumber + total
	counter += 1;
	newCounter = counter - 1

if naturalNumber > 0 and naturalNumber <= 10:
	print(f"The sum of the first {newCounter} natural numbers is: {total}")
	
if naturalNumber < 0 or naturalNumber > 10:
	print("Number is not a natural number")

