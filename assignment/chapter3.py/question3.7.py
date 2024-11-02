square = 0
cube = 0
number = 0
print("number\tsquare\tcube")
for number in range(0, 6, 1):
       square = number ** 2
       cube = number ** 3
       print(f"{number:>2}\t{square:>2}\t{cube:>2}")