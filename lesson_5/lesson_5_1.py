# Завдання 1 Ім'я змінної

# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.

# Змінна не може:

#         починатися з цифри,
#         складатися тільки з цифр,
#         містити великі літери, пропуск і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
#         бути жодним із зареєстрованих слів.

# При цьому ім'я змінної може складатися тільки з одного нижнього підкреслення "_".

# Список зареєстрованих слів можна взяти із keyword.kwlist.

# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно )

# _ => True
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True

###########

import string, keyword

name = input("Enter variable name: ")
result = True

if name[0].isdigit() or name.isdigit():
    result = False
if name in keyword.kwlist:
    result = False

for letter in name:
    if not result:
        break
    if letter.isupper():
        result = False
        break
    if letter == "_":
        continue
    if letter in string.punctuation or letter.isspace():
        result = False
        break

print(result)
