import math
import string
def get_divide_or_square(number):
	remainder = number%5
	quotient = number/5
	
	if remainder != 0:
		return remainder
	if remainder == 0:
		square_root = math.sqrt(quotient)
	if type(square_root) is int:
		return square_root
	if type(square_root) is float:
		return round(square_root, 3)
	
	 
			
	
	
		