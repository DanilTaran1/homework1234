number_str = input("Введите 4-х значное число")
number_full = int(number_str)               #1234 например
digit_4 = number_full%10
num_3 = number_full//10                     #123
digit_3 = num_3%10
num_2 = num_3//10                           #12
digit_2 = num_2%10
num_1 = num_2//10                           #1
digit_1 = num_1%10
print (digit_1)
print (digit_2)
print (digit_3)
print (digit_4)