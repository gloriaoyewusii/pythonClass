principal = float(input("Original amount invested: "))
annual_rate = float(input("Annual rate of return: "))
numberOfYears = float(input("Number of years: "))
rate = annual_rate/100

amount_deposit = (principal) * ((1 + rate) ** numberOfYears)
print(f"Amount deposited is {amount_deposit:.2f}")
