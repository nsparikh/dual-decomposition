'''
Adds each element of l1+l2
Both lists must be the same size.
'''
def add_lists(l1, l2):
	return [l1[i] + l2[i] for i in range(len(l1))]

'''
Subtracts each element of l2 from l1
Both lists must be the same size.
'''
def subtract_lists(list1, list2):
	return [l1[i] - l2[i] for i in range(len(l1))]

'''
Multiplies each element in l1 by a.
'''
def multiply_list(l1, a):
	return [l * a for l in l1]

'''
Divides each element in l1 by a.
'''
def divide_list(l1, a):
	return [l / a for l in l1]

'''
Divides each element of nested list l1 by a.
'''
def divide_nested_list(l1, a):
	return [[l / a for l in sub_list] for sub_list in l1]

'''
Multiplies each element of nested list l1 by a.
'''
def multiply_nested_list(l1, a):
	return [[l * a for l in sub_list] for sub_list in l1]

'''
Returns the index of the first non-zero element in the list.
'''
def find_non_zero(l1):
	for (i, l) in enumerate(l1):
		if l != 0:
			return i