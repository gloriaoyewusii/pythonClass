def get_palindrome(word):
	reverse = word[::-1]
	if word == reverse:
		return True
	else:
		return False	

word = "madam"
print(get_palindrome(word))
		