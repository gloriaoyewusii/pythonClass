products = []
numberOfItems = []
priceOfItems = []


def displayInvoice(customersName, nameOfCashier, products, numberOfItems, priceOfItems, discount, amountPaid):
	print("""
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312 HERBERT MACAULAY WAY, SABO YABA, LAGOS.
DATE: 18TH-DEC-22 7:25pm
""")
	print("Cashier: "+nameOfCashier+"\n")
	print("Customer's name: "+customersName+"\n")
	print("=================================================")
	print("ITEM\tQTY\tPRICE\tTOTAL(NGN)")
	print("-------------------------------------------------")
			
	billTotal = 0
	VAT = 17.50
	subTotal = 0
	for index in range(0, len(products)):
		print(f"{products[index]}\t{numberOfItems}\t{priceOfItems[index]:.2f}\t{numberOfItems[index] * priceOfItems[index]}\n")
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

	return products


def displayPromptToPay(customersName, nameOfCashier, products, numberOfItems, priceOfItems, discount):
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
		print(f"{products[index]}\t{numberOfItems}\t{priceOfItems[index]:.2f}\t{numberOfItems[index] * priceOfItems[index]}\n")
		subTotal += (numberOfItems[index] * priceOfItems[index])


	discount = (subTotal * (discount/100))
	VAT = (subTotal * (VAT/100))
	billTotal = (subTotal - discount + VAT)
	print("-------------------------------------------------")

	print(f"\tSub Total:{subTotal:.2f}\n\tDiscount:\t{discount:.2f}\n\tVAT:\t\t{VAT:.2f}\n")
	print("=================================================")
	print(f"\tBill Total:\t{billTotal:.2f}\n")

	print("=================================================")
	print(f"\n\tTHIS IS NOT A RECEIPT. KINDLY PAY {billTotal:.2f}")
	print("=================================================")

	amountPaid = int(input("How much did the customer give to you? - "))

	displayInvoice(customersName, nameOfCashier, products, numberOfItems, priceOfItems, discount, amountPaid)

	return amountPaid


def displaySystemQuestions(customersName, products, numberOfItems, priceOfItems):
	customersName = input("What is the customer's name? - ")
	productsBought = input("What did the user buy? - ")
	products.append(productsBought)

	productQuantity = int(input("How many pieces? - "))
	numberOfItems.append(productQuantity)

	productPrice = int(input("How much per unit? - "))
	priceOfItems.append(productPrice)

	print()
	addMoreItems = input("Do you want to add more items? - ")
	response = "Yes"
	if addMoreItems.lower() == response.lower():
		displaySystemQuestions(customersName, products, numberOfItems, priceOfItems)
	else:
		nameOfCashier = input("What is your name? - ")
		discount = int(input("How much discount will the customer get? - "))

	displayPromptToPay(customersName, nameOfCashier, products, numberOfItems, priceOfItems, discount)

	return products

customersName = "Gloria"
products = ["Parfait", "Chocolates"]
numberOfItems = [2, 3]
priceOfItems = [2100, 550]
discount = 8
nameOfCashier = "gee"

displaySystemQuestions(customersName, products, numberOfItems, priceOfItems)
displayPromptToPay(customersName, nameOfCashier, products, numberOfItems, priceOfItems, discount)
	

