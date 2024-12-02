products = []
numberOfItems = []
priceOfItems = []

def displaySystemQuestions(name, input, products, numberOfItems, priceOfItems):
	customersName = input("What is the customer's name? - ")
	productsBought = input("What did the user buy? - ")
	products.append(productsBought)

	productQuantity = int(input("How many pieces? - "))
	numberOfItems.append(productQuantity)

	productPrice = int(input("How much per unit? - "))
	priceOfItems.append(productPrice)

	print()
	addMoreItems = input("Do you want to add more items? - ")
	
	if addMoreItems.equalsIgnoreCase("Yes"):
		displaySystemQuestions(name, input, products, numberOfItems, priceOfItems)
	else:
		nameOfCashier = input("What is your name? - ")
		discount = int(input("How much discount will the customer get? - "))

	displayPromptToPay(customersName, nameOfCashier, input, products, numberOfItems, priceOfItems, discount)
	
def displayPromptToPay(customersName, nameOfCashier, input, products, numberOfItems, priceOfItems, discount):
	print("""
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312 HERBERT MACAULAY WAY, SABO YABA, LAGOS.
DATE: 18TH-DEC-22 7:25pm
""")			
	print(f"Cashier: {nameOfCashier}\n")
	print(f"Customer's name: {customersName}\n")
	print("=================================================")
	print("ITEM\tQTY\tPRICE\tTOTAL(NGN)")
	print("-------------------------------------------------")

			
	billTotal = 0
	VAT = 17.50
	subTotal = 0
	for index in range(0, len(products)):
		printf("{products[index]}\t{numberOfItems[index]}\t{priceOfItems[index]:.2f}\t{numberOfItems[index]:.2f * priceOfItems[index]:.2f\n")
		subTotal += (numberOfItems[index] * priceOfItems[index])


		discount = (subTotal * (discount/100))
		VAT = (subTotal * (VAT/100))
		billTotal = (subTotal - discount + VAT)
	print("-------------------------------------------------")

	print(f"\tSub Total:{subTotal:.2f}\n\tDiscount:\t{discount:.2f}\n\tVAT:\t\t{VAT:.2f}\n")
	print("=================================================")
	print(f"\tBill Total:\t{billTotal:.2f}\n")

	print("=================================================")
	print("\n\tTHIS IS NOT A RECEIPT. KINDLY PAY "+billTotal)
	print("=================================================")

	amountPaid = int(input("How much did the customer give to you? - "))

	displayInvoice(customersName, nameOfCashier, input, products, numberOfItems, priceOfItems, discount, amountPaid)


def displayInvoice(customersName, nameOfCashier, input, products, numberOfItems, priceOfItems, discount, amountPaid):
		print("""
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312 HERBERT MACAULAY WAY, SABO YABA, LAGOS.
DATE: 18TH-DEC-22 7:25pm
""")
		print("Cashier: "+nameOfCashier+"\n")
		print("Customer's name: "+customersName+"\n")
		println("=================================================")
		println("ITEM\tQTY\tPRICE\tTOTAL(NGN)")
		println("-------------------------------------------------")
			
		billTotal = 0
		VAT = 17.50
		subTotal = 0
		for index in range(0, len(products)):
			print(f"{products[index]}\t{numberOfItems[index]}\t{priceOfItems[index]:.2f}\t{numberOfItems[index]:.2f * priceOfItems[index]:.2f}\n")
			subTotal += (numberOfItems[index] * priceOfItems[index])
				
		discount = (subTotal * (discount/100))
		VAT = (subTotal * (VAT/100))
		billTotal = (subTotal - discount + VAT)
		balance = amountPaid - billTotal
		print("-------------------------------------------------")

		print(f"\tSub Total:{subTotal:.2f}\n\tDiscount:\t{discount:.2f}\n\tVAT:\t\t{VAT:.2f}\n")
		print("=================================================")
		print(f"\tBill Total:\t{billTotal:.2f}\n\tBalance:\t{balance:.2f}\n")
	
		print("=================================================")
		print("\n\tTHANK YOU FOR YOUR PATRONAGE")
		print("=================================================")

		return amountPaid

			

	


	
	