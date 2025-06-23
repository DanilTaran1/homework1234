lst = [12, 3, 4, 10]
if lst == []:
    print(lst)
else:
    removed_a = lst.pop(-1)
    lst.insert(0,removed_a)
    print(lst)