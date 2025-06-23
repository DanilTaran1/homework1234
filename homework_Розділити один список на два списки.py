lst = []
if len(lst) == 1:
    result = [lst ,[]]
    print(result)
else:
    cutted = len(lst)// 2
    print(cutted)
    print([lst[:-cutted], lst[-cutted:]])