number_str = input("Введите 5-и значное число")
number_full = int(number_str)
digit_5 = number_full%10
num_4 = number_full//10
digit_4 = num_4%10
num_3 = num_4//10
digit_3 = num_3%10
num_2 = num_3//10
digit_2 = num_2%10
num_1 = num_2//10
digit_1 = num_1%10
print(digit_5,digit_4,digit_3,digit_2,digit_1)