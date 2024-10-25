start = int(input("number: "))
end = int(input("ending number: "))
divisor = int(input("divisor: "))
count = 0
 

while start <= end:
	if start % divisor == 0:
		count+=1
	start+=1

print(count)
	

