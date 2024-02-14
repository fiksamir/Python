# Завдання 2 Перевірка на парність.

# ﻿Завдання ускладнюється. 

# Ваша функція is_even, як і раніше, повинна повертати True якщо число парне, або False якщо число непарне, але при цьому НЕ МОЖНА використовувати ділення у функції,
#  та дії пов'язані з ним. Тобто. заборонено використовувати /, //, % та divmod

# Складність ще полягає і в тому, щоб знайти рішення, яке не залежало б від розміру числа :)

# Вхідні дані: Ціле число.

# Вихідні дані: True або False

# def is_even(number):
#     pass


# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
##############

def is_even(number:int) -> bool:
    even_tuple = ("0","2","4","6","8")
    last_digit = str(number)[-1]

    if last_digit in even_tuple:
        return True
        
    return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')