total = 0
counter = 1
taxAmount = 0
nameCounter = 1
   
while nameCounter <= 3 and counter <= 3:
     name = input("Enter name: ")
     nameCounter = nameCounter + 1
     citizenEarning = float(input("Earnings: "))            
     counter = counter + 1

     if citizenEarning <= 30000:
     	taxAmount = citizenEarning * 0.15
       
     	if citizenEarning > 30000:
     		taxAmount = citizenEarning * 0.20
     total = total + taxAmount
       
print(f"The total tax amount for the three citizens is: {total:.2f}")