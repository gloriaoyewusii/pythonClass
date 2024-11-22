def get_vowels(string):
	vowel_counter = 0
	for characters in string:
		if characters == 'a' or characters == 'e' or characters == 'i' or characters == 'o' or characters == 'u':
			vowel_counter = vowel_counter + 1
	return vowel_counter

string = "Python is sweet"
print(get_vowels(string))