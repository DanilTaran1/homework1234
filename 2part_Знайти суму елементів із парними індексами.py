lst = [0, 1, 7, 2, 4, 8]
if lst == []:
    print(0)
else:
    total = 0
    a = lst[::2]
    b = lst.pop()
    for l in a:
        total = total + l
        c = total * b
    print(c)