def get_common_element(list1, list2:list):
	for element in list1:
		if element in list2:
			return element

list1 = [1, 2, 3]
list2 = [3, 4, 5]
print(get_common_element(list1,list2))