import string
import keyword
my_string = input("Enter a string: ")
if my_string[0].isdigit():
    print("False")
if any(my_string.isupper() for my_string in my_string):
    print("False")
if my_string in keyword.kwlist:
    print("False")
if any(my_string for i in string.punctuation):
    print("False")
