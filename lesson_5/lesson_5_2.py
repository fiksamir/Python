# Завдання 2 Модифікувати калькулятор

# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче

# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення - якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.
##########

def check_exit():
    str = input("Continue working? (yes/y): ")
    if str == "yes" or str == "y":
        return True
    else:
        return False

print("Hello! This is simple Python calculator.")

while True:
    number_1 = input("Enter first number: ")  
    number_2 = input("Enter second number: ")    

    if len(number_1) == 0 or len(number_2) == 0:
        print("Error! Unknown number")
        continue
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
            print(f"{number_1} / {number_2} = {number_1 / number_2}")            

    if check_exit():
        continue
    else:
        break
