import string
my_string = input("Enter a string: ")
for i in string.punctuation:
    my_string = my_string.replace(i, "")
my_string_1 = my_string.title()
my_string_2 = my_string_1.replace(" ", "")
my_string_3 = "#" + my_string_2
my_string_4 = my_string_3[:140]
print(my_string_4)




digit = int(input("Введіть кількість секунд: "))
sec = digit % 60
minutes = digit // 60
minutes_1 = minutes % 60
hours = minutes // 60
hours_1 = hours % 24
days = hours // 24
days = str(days)
hours_1= str(hours_1)
minutes_1= str(minutes_1)
sec = str(sec)
if days.startswith("1") and days.endswith("2") or days.endswith("3") or days.endswith("4") or days.endswith("1"):
    print(days, "Днів", hours_1.zfill(2), ":", minutes_1.zfill(2), ":", sec.zfill(2))
elif days.endswith("2") or days.endswith("3") or days.endswith("4"):
    print(days, "Дні", hours_1.zfill(2), ":", minutes_1.zfill(2), ":", sec.zfill(2))
elif days.endswith("1"):
    print(days, "День", hours_1.zfill(2), ":", minutes_1.zfill(2), ":", sec.zfill(2))
else:
    print(days,"Днів",hours_1.zfill(2),":",minutes_1.zfill(2),":",sec.zfill(2))
