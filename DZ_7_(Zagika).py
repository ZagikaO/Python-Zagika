from random import randint

#####################################
# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
my_list = [randint(1, 100) for _ in range(20)]
print("1) random list of 20 values: ", my_list)

#####################################
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси
def create_coordinates() -> tuple:
    return tuple([randint(-10, 10) for _ in range(2)])

triangle = {"A": create_coordinates(),
            "B": create_coordinates(),
            "C": create_coordinates()}
print("2) dict triangle: ", triangle)

#####################################
# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***
def my_str_print(str: str):
    print("***"+str+"***")

print("3) resulr for function my_print: ")
my_str = "I'm the string"
my_str_print(my_str)
# print(my_str)

#####################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
my_dict_list = [{"name": "John", "age": 15},
                {"name": "James", "age": 5},
                {"name": "Jordan", "age": 5},
                {"name": "Joseph", "age": 70},
                {"name": "Jessica", "age": 37},
                {"name": "Jack", "age": 45}]

# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# youngest_man
min_age = min(my_dict["age"] for my_dict in my_dict_list)
for my_dict in my_dict_list:
    if my_dict["age"] == min_age:
        print("4a) the youngest man: ", my_dict["name"])

# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# longest_name
longest_name = max(len(my_dict["name"]) for my_dict in my_dict_list)
for my_dict in my_dict_list:
    if len(my_dict["name"]) == longest_name:
        print("4b) longest name: ", my_dict["name"])

# в) Посчитать среднее количество лет всех людей из списка.
# average_years
average_years = sum(my_dict["age"] for my_dict in my_dict_list)/len(my_dict_list)
print("4c) average years: ", average_years)

#####################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
dict_1 = {"name": "Jessica", "lastname": "Parker", "else_": "qwerty", "age": 37, }
dict_2 = {"name": "John", "age": 15, "child": 3}
print("5) dict_1 =", dict_1)
print("   dict_2 =", dict_2)

# а) Создать список из ключей, которые есть в обоих словарях.
common_keys = list(set(dict_1.keys()).intersection(set(dict_2.keys())))
print("5a) common keys =", common_keys)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
unique_keys_1 = []
for keys in dict_1.keys():
    if keys not in dict_2.keys():
        unique_keys_1.append(keys)
print("5b) unique_keys_1 =", unique_keys_1)
#
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
unique_dict_1 = {}
for key, value in dict_1.items():
    if key not in dict_2.keys():
        unique_dict_1[key] = value
print("5c) unique_dict =", unique_dict_1)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]}
def create_general_dict(dict1: dict, dict2: dict, dict3: dict):
    for key, value in dict1.items():
        if key in dict2.keys():
            dict3.setdefault(key, []).append(value)
        else:
            dict3[key] = value
    return dict3

general_dict = {}
general_dict_result = create_general_dict(dict_1, dict_2, general_dict)
general_dict_result = create_general_dict(dict_2, dict_1, general_dict)
print("5d) general_dict =", general_dict_result)