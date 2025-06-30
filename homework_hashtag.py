import string
my_string = input("Enter a string: ")
for i in string.punctuation:
    my_string = my_string.replace(i, "")
my_string_1 = my_string.title()
my_string_2 = my_string_1.replace(" ", "")
my_string_3 = "#" + my_string_2
my_string_4 = my_string_3[:140]
print(my_string_4)
