import string


def first_word(text: str) -> str:
    for char in text:
        if char in string.punctuation:
            text = text.replace(char, ' ')
        elif "'" in text:
            return text.split()[0]
    return text.split()[0]


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
