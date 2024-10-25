weightInPounds = float(input("Enter a weight in pound: "))

weightInKilos = 0.45359237 * weightInPounds

heightInInches = float(input("Enter a height in inches: "))

heightInMeters = 0.0254 * heightInInches

BMI = weightInKilos / (heightInMeters * heightInMeters)

print(f"{BMI:.4f}")