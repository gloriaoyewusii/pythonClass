contacts = [[], [], []]
def get_first_name(first_name):
	first_name = input("First Name: ")
	return first_name

def get_last_name(last_name):
	last_name = input("Last Name: ")
	return last_name

def get_phone_number(mobile_number):
	mobile_number = input("Mobile Number: ")
	return mobile_number

def selectMenu(options):
	print("Contacts\n")
	print("Contacts Menu\n")
	options = int(input("1. Add Contact\n2. Remove Contact\n3. Search Contact\n4. Edit Contact\n"))
	match options:
		case 1: 
			print("Add Contact")
			get_first_name(first_name)
			for index in contacts[0]:
				contacts[0][index].append(first_name)
			get_last_name(last_name)
			for index in contacts[1]:
				contacts[1][index].append(last_name)
			get_phone_number(mobile_number)
			for index in contacts[2]:
				contacts[2][index].append(mobile_number)
				

		case 2: 
			print("Remove Contact")
			get_first_name(first_name)
			for index in contacts[0]:
				contacts[0][index].remove(first_name)
			get_last_name(last_name)
			for index in contacts[1]:
				contacts[1][index].remove(last_name)
			get_phone_number(mobile_number)
			for index in contacts[2]:
				contacts[2][index].remove(last_name)
		case 3: 
			print("Search Contact")
			choice = int(input("\n1. Find contact by first name\n2. Find contact by last name\n3. Find contact by mobile number"))
			match choice:
				case 1: 
					print("Find contact by first name")
					for index in contacts[0]:
						if contacts[0][index] in contacts[0]:
							print("Contact found")
							print(contacts[0][index])
						if contacts[0][index] not in contacts[0]:
							print("Contact not found")
				case 2: 
					print("Find contact by last name")
					for index in contacts[1]:
						if contacts[1][index] in contacts[1]:
							print("Contact found")
							print(contacts[1][index])
						if contacts[1][index] not in contacts[1]:
							print("Contact not found")
				case 3: 
					print("Find contact by mobile number")
					for index in contacts[2]:
						if contacts[2][index] in contacts[1]:
							print("Contact found")
							print(contacts[2][index])
						if contacts[2][index] not in contacts[2]:
							print("Contact not found")
		case 4: 
			print("Edit Contact")
			for index in contacts[0]:
				contacts[0][index].pop()
				contacts[0][index].sort()
			for index in contacts[1]:
				contacts[1][index].pop()
				contacts[1][index].sort()
			for index in contacts[2]:
				contacts[2][index].sort()
				contacts[2][index].pop()
	return options

first_name = ["feyre", "esther", "gracie", "Dara"]
last_name = ["smith", "white", "west", "grey"]
mobile_number = ["08023458976", "09045678954", "07021340989", "09176879870"]
options = ""

print(selectMenu(options))



