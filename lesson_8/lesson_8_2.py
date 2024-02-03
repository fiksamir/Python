# Завдання 2

# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел, знаходить серед них унікальне число та повертати його.
# Унікальне число - це число, яке зустрічається в списку один раз. Випадок, коли в одному списку буде кілька унікальних чисел, перевіряти не потрібно.
# Приклад:

# def find_unique_value(some_list):
#     pass

# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")
#################

def find_unique_value(some_list):
    unique_dict = {}

    for value in some_list:   
        if value in unique_dict:        
            unique_dict[value] += 1
        else:        
            unique_dict[value] = 1

    for el, count in unique_dict.items():
        if count == 1:
            return el


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("OK")