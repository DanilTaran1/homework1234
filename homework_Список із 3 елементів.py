import random
lst = [random.randint(1,10) for i in range(random.randint(3, 10))]
#lst = [1,2,3]
if len(lst) == 3:
    first = lst.pop(2)
    second = lst.pop(0)
    third = lst.pop(-1)
    newlst = [second,first,third]
    print(newlst)
else:
    a = lst.pop(2)
    b = lst.pop(0)
    c = lst.pop(-2)
    new_lst = [b,a,c]
    print (new_lst)
