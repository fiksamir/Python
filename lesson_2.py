# отримуємо число
number = int(input("Введіть 4-значне число: "))

# виводим перший розряд
print(number // 1000) 

# зменшуємо число на перший розряд
number -= (number // 1000 ) * 1000

# повторюємо для інших розрядів
print(number // 100)
number -= (number // 100) * 100

print(number // 10)
number -= (number // 10) * 10

print(number // 1)

