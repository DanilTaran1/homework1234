lst = [0, 1, 7, 2, 4, 8]
if lst == []:
    print(0)
else:
    a = lst[::2]
    b = lst.pop()
    c = sum(a) * b
    print (c)