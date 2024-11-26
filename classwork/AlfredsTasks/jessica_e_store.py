product_name = ["Laptop", "Phone", "Headphone"]
product_price = ["$1000", "$500", "$100"]
cart = []

def main_menu():
	print("Main menu\n1. View products\n2. Add to Cart\n3. Remove from cart\n4. View cart\n5. Checkout\n6. Exit")
	selection = int(input("Select an option: "))
	match selection:
		case 1: print("View products")
		case 2: print("Add to cart")
		case 3: print("Remove from cart")
		case 4: print("View cart")
		case 5: print("Checkout")
		case 6: print("Exit")

def view_products():
	print("1. Laptops\n2. Phones\n3. Headphones")
	viewSelection = int(input("Select an option: "))
	match viewSelection:
		case 1: print("Laptop - $1000")
		case 2: print("Phone - $500")
		case 3: print("Headphones - $100")

def add_to_cart(cart, products):
	if viewSelection == 1:
		cart.append(product_name[0])
		print("Laptop has been added to your cart.")
	elif viewSelection == 2:
		print("Phone has been added to your cart.")
	elif viewSelection == 3:
		print("Headphone has been added to your cart.")
		
main_menu()
view_products()
add_to_cart(cart, products)	
	
