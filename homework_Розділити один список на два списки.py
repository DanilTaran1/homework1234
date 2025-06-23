lst = [1,2,3,4,5]
if len(lst) == 1:
    result = [lst ,[]]
    print(result)
else:
    cutted = len(lst) // 2
    print (cutted)
    print([lst[:-cutted], lst[-cutted:]])