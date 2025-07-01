import string
letters = string.ascii_letters
my_str = input("Enter a stirng:")
a,b = my_str.split("-")
lt_1, lt_2 = letters.index(a), letters.index(b)
result = letters[lt_1:lt_2+1]
print(result)
