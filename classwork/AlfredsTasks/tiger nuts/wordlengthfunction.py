def get_word_length(words:list):
	for count in range(0, len(words)):
		for word in words:
			for counter in word:
				return counter



words = ["apple", "cashews", "cherry"]
print(get_word_length(words))