integer_number = int(input("Number: "))
binary_number = " "


while integer_number > 0:
    remainder = integer_number % 2
    binary_number = str(remainder) + binary_number
    integer_number =  integer_number // 2

print(binary_number)




