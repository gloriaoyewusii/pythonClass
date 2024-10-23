weightInPounds = float(input("weightInPounds: "))
	
weightInKilos = 0.45359237 * weightInPounds
print("Weight in Kilograms is: ", weightInKilos);

heightInInches = float(input("Enter a height in inches: "))

heightInMeters = 0.0254 * heightInInches
print("Height in Meters is: ", heightInMeters)

BMI = weightInKilos / (heightInMeters * heightInMeters);
print(f"BMI is: {BMI:.4f}")
