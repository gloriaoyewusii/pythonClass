import math
latitude1 = float(input("Enter latitude of coordinate 1: "))
longitude1 = float(input("Enter the longitude of coordinate 1: ")) 
latitude2 = float(input("Enter latitude of coordinate 2: "))
longitude2 = float(input("Enter the longitude of coordinate 2: \n"))
radius = float(input("Enter radius of the earth"))


earthsdistance = radius * (math.acos)((math.sin(latitude1)) * math.cos(latitude2) * math.cos(latitude1) * math.cos(latitude2) * math.cos(longitude1 - longitude2))

print("The distance between two points is: ", earthsdistance)