# Завдання 2 Перевірити чи є парним чи ні

# Ваша функція is_even повинна повертати True якщо число парне, і False якщо число непарне.

# Вхідні дані: Ціле число.

# Вихідні дані: Логічний тип.

# def is_even(digit):
#     """ Перевірка чи є парним число """
#     pass
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')
##############

def is_even(digit):
    if digit % 2 == 0:
        return True
    else: 
        return False

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')