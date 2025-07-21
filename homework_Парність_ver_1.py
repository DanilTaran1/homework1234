def is_even(number: int):
    iterable = str(number)
    if iterable.endswith('0') or iterable.endswith('2') or iterable.endswith('4') or iterable.endswith('6') or iterable.endswith('8'):
        return True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'