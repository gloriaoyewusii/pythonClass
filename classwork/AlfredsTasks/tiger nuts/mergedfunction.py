def get_merged_list(list1, list2):
	merged_list = list1 + list2
	merged_list.sort()

	return merged_list

list1 = [1, 3, 5]
list2 = [2, 4, 6]

print(get_merged_list(list1,list2))
