import string
import keyword
x = string.punctuation
y = x.replace("_","")
my_str = input("Enter a string: ")
if my_str[0].isdigit():
    print("False")
elif my_str in keyword.kwlist:
    print("False")
elif any(i.isupper() for i in my_str):
    print("False")
elif any(i in y for i in my_str):
    print("False")
elif my_str == "_":
    print("True")
elif "__" in my_str:
    print("False")
elif my_str.startswith("_") and my_str.endswith("_"):
    print("False")
elif " " in my_str:
    print("False")
else:
    print("True")