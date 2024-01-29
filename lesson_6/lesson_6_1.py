# Завдання 1

# Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]

# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.

# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.

# в) Порахувати середню вік усіх людей із початкового списку.
##############
list = [
    {
        "name": "John",
        "age": 55,
    },
    {
        "name": "Jack",
        "age": 45,
    },
    {
        "name": "Nick",
        "age": 15,
    },
    {
        "name": "Bob",
        "age": 35,
    },
    {
        "name": "Anna",
        "age": 15,
    },
    {
        "name": "Helga",
        "age": 44,
    },
    {
        "name": "Denys",
        "age": 35,
    },
]
young_list = []
long_name_list = []
min_age = 1000
max_name_len = 0
av_age = 0

for person in list:
    age = person.get("age") 
    name_len = len(person.get("name"))
    av_age += age

    # а
    if age == min_age:
        young_list.append(person.get("name"))
    elif age < min_age:
        young_list.clear()
        young_list.append(person.get("name"))
        min_age = age    
    # б
    if name_len == max_name_len:
        long_name_list.append(person.get("name"))
    elif name_len > max_name_len:
        long_name_list.clear()
        long_name_list.append(person.get("name"))
        max_name_len = name_len  

# в
av_age = av_age/len(list)

print(young_list)
print(long_name_list)
print(round(av_age))