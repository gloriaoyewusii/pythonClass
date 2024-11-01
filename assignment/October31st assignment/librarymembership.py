returnTime = int(input("Number of days taken to return book: "))
	
if returnTime == 5:
	print("The fine is 50 paise")
else: 
	if returnTime > 5 and returnTime <= 10:
		print("The fine to be paid is: One rupee")
	else:
		if returnTime > 10:
			print("The fine to be paid is: 5 rupees")
		else: 
			if returnTime > 30:
				print("Membership terminated")