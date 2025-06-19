number_1 = int(input("Введите число: "))
number_2 = int(input("Введите второе число: "))
action = input("Введите знак действия которое хотите выполнить: ")
if action == "+":
    result = number_1+number_2
    print (result)
elif action == "-":
    result = number_1-number_2
    print (result)
elif action == "*":
    result = number_1*number_2
    print (result)
elif action == "/":
    result = number_1/number_2
    print(result)
else:
    action == '%'
    print ("Недопустимое значение")