lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for a in lst:
    a = lst.index(0)
    b = lst.pop(a)
    c = lst.append(b)
print(lst)

