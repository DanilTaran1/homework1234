def add_one(some_list):
    removed = "".join(str(i) for i in some_list)
    add_one_my= int(removed) + 1
    result = list(str(add_one_my))
    return [int (i) for i in result]
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")