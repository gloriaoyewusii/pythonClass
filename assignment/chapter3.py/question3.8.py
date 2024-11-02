number = int(input("Enter a dummy number here to start: "))
sum = 0
average = 0
product = 1
counter = 1
largestNumber = number
smallestNumber = number


for number in range(4):
    number = int(input("Enter an integer: "))
    counter = counter + 1
    
    sum = sum + number
    average = sum/counter
    product = number * product
    if number > largestNumber:
       largestNumber = number
    elif number < smallestNumber:
       smallestNumber = number
    
    
print("The sum is: ", sum)
print("The average is: ", average)
print("The product is: ", product)
print("The largest number is: ", largestNumber)
print("The smallest number is: ", smallestNumber)






