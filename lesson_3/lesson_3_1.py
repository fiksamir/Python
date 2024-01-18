# Завдання 1 Найпростіший калькулятор

# Програма має виконувати прості математичні дії (+, -, *, /). Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма, виходячи з дії, обчислює та друкує результат.

# Зробити перевірку на те, що при діленні дільник не дорівнює 0!
########################################

print("Hello! This is simple Python calculator.")
number_1 = input("Enter first number:")
number_2 = input("Enter second number:")

if len(number_1) == 0 or len(number_2) == 0:
    print("Error! Unknown number")
else:
    number_1 = float(number_1)
    number_2 = float(number_2)

action = input("Enter one action (+|-|/|*):")

if (action not in ("+","-","*","/")):
    print("Wrong action!")  
elif action == "+":
    print(f"{number_1} + {number_2} = {number_1 + number_2}")
elif action == "-":
    print(f"{number_1} - {number_2} = {number_1 - number_2}")
elif action == "*":
    print(f"{number_1} * {number_2} = {number_1 * number_2}")
elif action == "/":
    if (number_2 == 0):
       print("Error! Division by zero!")
    else: 
       print(f"{number_1} + {number_2} = {number_1 / number_2}")