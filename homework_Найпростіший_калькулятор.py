while True:
    number_1 = int(input("Введите число: "))
    number_2 = int(input("Введите второе число: "))
    action = input("Введите знак действия которое хотите выполнить: ")
    if action == "+":
        result = number_1 + number_2
        print(result)
    elif action == "-":
        result = number_1 - number_2
        print(result)
    elif action == "*":
        result = number_1 * number_2
        print(result)
    elif action == "/" and number_2 == 0:
        print("Недопустимое значение (деление на ноль)")
    else:
        result = number_1 / number_2
        print(result)
    print("Продолжить работу?")
    answer = input()
    if answer == "yes" or answer == "y":
        continue
    elif answer == "no" or answer == "n":
        break


