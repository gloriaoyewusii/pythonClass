def get_space(string):
	removal = string.insert(" ", "")
	return removal

string = ("hello world")
print(get_space(string))