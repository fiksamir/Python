# Завдання 2

# Дано два словники my_dict_1 і my_dict_2.

# а) Створити список із ключів, які є в обох словниках.

# б) Створити список із ключів, які є у першому, але немає у другому словнику.

# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.

# г) Об'єднати ці два словники у новий словник за правилом:

# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,

# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},

# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

####################

my_dict_1 = {1:1, 2:2, 3:56, 11:23}
my_dict_2 = {11:11, 2:22, 5:44}

set_1 = set(my_dict_1.keys())
set_2 = set(my_dict_2.keys())

#а
union_list = list(set_1.union(set_2)) 
print(union_list)

#б
dif_list = list(set_1.difference(set_2)) 
print(dif_list)

# в
dict_3 = {}
for i in dif_list:
    dict_3[i] = my_dict_1[i]

print(dict_3)

# г
dict_4 = dict.fromkeys(union_list)
for i in dict_4:
    value_1 = my_dict_1.get(i)
    value_2 = my_dict_2.get(i)
    if value_1 == None:
        dict_4[i] = value_2
    elif value_2 == None:
        dict_4[i] = value_1
    else:
        dict_4[i] = [value_1, value_2]

print(dict_4)


