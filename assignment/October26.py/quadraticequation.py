import math
import cmath
coefficient1 = int(input("Enter first number: "))
coefficient2 = int(input("Enter second number: "))
coefficient3 = int(input("Enter third number: "))

coefficient2_square = coefficient2 * coefficient2
squareRootExpression = 4 * coefficient1 * coefficient3
discriminant = coefficient2_square - squareRootExpression

root_first = ((- coefficient2) + cmath.sqrt(discriminant))/(2 * coefficient1)
if discriminant < 0:
	print(f"First root is: {root_first}")
	print("Root is complex")
		 
elif discriminant > 0:
	print(f"First root is: {root_first}")
	print("Root is real and distinct")
elif discriminant == 0:
	print(f"First root is: {root_first}")
	print("Root is real and equal")
root_second = ((- coefficient2) - cmath.sqrt(discriminant))/(2 * coefficient1);
if discriminant < 0:
	print(f"Second root is: {root_second}")
	print("Root is complex")
elif discriminant > 0:
	print(f"Second root is: {root_second}")
	print("Root is real and distinct")
elif discriminant == 0:
	print(f"Second root is: {root_second}")
	print("Root is real and equal")

		