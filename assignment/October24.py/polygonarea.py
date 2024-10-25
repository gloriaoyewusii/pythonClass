import math
length_polygon = float(input("Enter the length of a polygon: "))
print("Length of a polygon is: ", length_polygon)
number_sides_polygon = float(input("Enter the number of sides of a polygon: "))
print("Number of polygon sides is: ", number_sides_polygon)

area = number_sides_polygon * length_polygon * length_polygon/(4 * (math.tan)(math.pi/number_sides_polygon))

print("Area is: ", area)

