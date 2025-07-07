def common_elements():
	lst_1 = list(range(0, 101, 3))
	lst_2 = list(range(0, 101, 5))
	set_1 = set(lst_1)
	set_2 = set(lst_2)
	intersection_set = set_1.intersection(set_2)
	return intersection_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
