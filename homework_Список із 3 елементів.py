import random
lst = [random.randint(1,10) for i in range(random.randint(3, 10))]
#lst = [1,2,3]
if len(lst) == 3:
    first = lst.pop(2)
    second = lst.pop(-2)
    third = lst.pop(0)
    newlst = [first,second,third]
    newlst.sort()
    print(newlst)
else:
    a = lst.pop(2)
    b = lst.pop(0)
    c = lst.pop(-2)
    new_lst = [a,b,c]
    new_lst.sort()
    print (new_lst)
#print(lst)