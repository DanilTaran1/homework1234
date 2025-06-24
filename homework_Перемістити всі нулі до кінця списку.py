lst = [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9]
a = 0
for a in lst:
    a = lst.index(0)
    b = lst.pop(a)
    c = lst.append(b)
print(lst)

