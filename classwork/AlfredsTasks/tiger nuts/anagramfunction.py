def get_anagram(string1, string2):
	for characters in string1:	
		if characters in string2:
			return True
		else:
			return False
