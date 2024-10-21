Principal_Amount = float(input("Enter Principal amount: "))


Annual_Interest_Rate = float(input("Enter the annual interest rate: "))


Duration = int(input("Enter the duration of the loan: "))


Monthly_Interest_Rate = (Annual_Interest_Rate/100)/12

Monthly_Duration = Duration * 12

Monthly_Payment_Value = Principal_Amount * Monthly_Interest_Rate * ((1 + Monthly_Interest_Rate) ** Monthly_Duration) / (((1 + Monthly_Interest_Rate) ** Monthly_Duration) - 1)

print(f"{Monthly_Payment_Value:.2f}")