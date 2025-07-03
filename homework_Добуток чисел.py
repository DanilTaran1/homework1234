full_digit = int(input("Enter a number:"))
s_digit = full_digit
while s_digit > 9:
    digit_1 = s_digit % 10
    digit_2 = s_digit // 10
    digit_3 = digit_2 % 10
    digit_4 = s_digit // 100
    digit_5 = digit_4 % 10
    if digit_5 == 0:
        digit_5 = 1
    s_digit = digit_1 * digit_3 * digit_5
print(s_digit)