def get_acronym(words):
	split_words = words.split()
	acronym = ""
	for word in split_words:
		acronym+=word[0]
	return acronym
	
	
	

words = "Portable Network Graphics"
print(get_acronym(words))