import string
def is_palindrome(text):
    my_str = ''.join(char for char in text if char not in string.punctuation)
    result_string = my_str.lower().replace(" ", "")
    if result_string == result_string[::-1]:
        return True
    else:
        return False
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")