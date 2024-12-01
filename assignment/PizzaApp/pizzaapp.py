def getPizzaFor(numberOfGuests):

	numberOfBoxes = 1
	price = 1
	numberOfGuests = int(input("Number of people: \n"))

	pizzaType = int(input("Select your preferred pizza type:\n1. Sapa size\n2. Small money\n3. Big boys\n4. Odogwu\nSelection: "))

	match pizzaType:
		case 1: print("Pizza type: Sapa size\n")
		case 2: print("Pizza type: Small money\n")
		case 3: print("Pizza type: Big boys\n")
		case 4: print("Pizza type: Odogwu\n")

	

	numberOfSlices = [4, 6, 8, 12]
	pricePerBox = [2500, 2900, 4000, 5200]
	slicesToBuy = 1

	for index in range(0, 1):
		if pizzaType == 1:
			slicesToBuy = numberOfGuests 

			numberOfBoxes = slicesToBuy // numberOfSlices[index]

			if slicesToBuy % numberOfSlices[index] > 0:
				numberOfBoxes += 1

			price = numberOfBoxes * pricePerBox[index]

			print(f"Number of boxes of pizza to buy: {numberOfBoxes} boxes\n")

			remainingSlices = (numberOfBoxes * numberOfSlices[index]) - numberOfGuests

	
		elif pizzaType == 2:
			slicesToBuy = numberOfGuests 

			numberOfBoxes = slicesToBuy // numberOfSlices[index+1]

			if slicesToBuy % numberOfSlices[index+1] > 0:
				numberOfBoxes += 1

			price = numberOfBoxes * pricePerBox[index]

			print(f"Number of boxes of pizza to buy: {numberOfBoxes} boxes\n")

			remainingSlices = (numberOfBoxes * numberOfSlices[index+1]) - numberOfGuests;


		elif pizzaType == 3:
			slicesToBuy = numberOfGuests 

			numberOfBoxes = slicesToBuy // numberOfSlices[index+2]

			price = numberOfBoxes * pricePerBox[index]

			if slicesToBuy % numberOfSlices[index+2] > 0:
				numberOfBoxes += 1

			print(f"Number of boxes of pizza to buy: {numberOfBoxes} boxes\n")

			remainingSlices = (numberOfBoxes * numberOfSlices[index+2]) - numberOfGuests;


		elif pizzaType == 4:
			slicesToBuy = numberOfGuests 

			numberOfBoxes = slicesToBuy // numberOfSlices[index+3]

			if slicesToBuy % numberOfSlices[index+3] > 0:
				numberOfBoxes += 1

			price = numberOfBoxes * pricePerBox[index+3]

			print(f"Number of boxes of pizza to buy: {numberOfBoxes} boxes\n")
		
			remainingSlices = (numberOfBoxes * numberOfSlices[index+3]) - numberOfGuests;

		print(f"Number left over slices after serving = {remainingSlices} slices\n")
		
			
	print(f"Price = {price}")

	return price

