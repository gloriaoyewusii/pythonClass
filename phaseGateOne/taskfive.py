user_input = int(input("Enter an integer for today's day of the week: \n0. Sunday\n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday"))

future_day = ""
match user_input:
	case 0: print(f"Sunday")

	case 1: print(f"Monday")

	case 2:print(f"Wednesday")


	case 3: print(f"Thursday")


	case 4: print(f"Friday")


	case 5: print(f"Saturday")


	case 6: print(f"Sunday")


 

elapsed_days = int(input("Enter the number of days after today for a future day: "))

for index in range(1, elapsed_days):
	future_day = user_input
print(future_day)

