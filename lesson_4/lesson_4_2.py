# Завдання 2

# Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд], потім перемножити цю суму на останній елемент вхідного масиву.

# Не забудьте, що перший елемент масиву має індекс 0.

# Для порожнього масиву результат завжди 0.

# Пояснення:

# [0, 1, 7, 2, 4, 8] -> (0 + 7 + 4) * 8 = 88

# [1, 3, 5] -> 30
# [6] -> 36
# [] -> 0

# Для перевірки коректності роботи Вашого коду використовуйте приклади вище. Робити запит на введення даних від користувача не потрібно.
########################

main_list = [
    [0, 1, 7, 2, 4, 8],
    [1, 3, 5],
    [6],
    []
]

for list in main_list:
    result = 0
    for i in range(0, len(list), 2):
        result += list[i] 
    if len(list) > 0:    
        result *= list[-1]
    print(f"{list} -> {result}")