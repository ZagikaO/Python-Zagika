####################################
# # 1. Дан список строк my_list. Создать новый список в который поместить
# # элементы из my_list по следующему правилу:
# # Если строка стоит на нечетном месте в my_list, то ее заменить на
# # перевернутую строку. "qwe" на "ewq".
# # Если на четном - оставить без изменения.
# # Задание сделать с использованием enumerate.
#
# my_list = ["Apple", "Pear", "Apricot", "Ginger", "Avocado", "Orange"]
# my_new_list = []
# for index, value in enumerate(my_list):
#     if index % 2:
#         my_new_list.append(value[::-1])
#     else:
#         my_new_list.append(value)
# print(my_new_list)
# print(my_list)



####################################

# # 2. Дан список строк my_list. Создать новый список в который поместить
# # элементы из my_list у которых первый символ - буква "a".
#
# my_list = ["Apple", "pear", "Apricot", "ginger", "avocado", "orange"]
# # symbol = "a"
# my_list_1 = [item for item in my_list if item.startswith("a")]
# # my_list_1 = [item for item in my_list if (item[0] == "a")]
# print(my_list_1)



####################################
# # 3. Дан список строк my_list. Создать новый список в который поместить
# # элементы из my_list в которых есть символ - буква "a" на любом месте.
# #
# my_list = ["Apple", "Pear", "Apricot", "Ginger", "Avocado", "Orange"]
# my_new_list = [item for item in my_list if item.count("a")]
# print(my_new_list)
# print(my_list)



####################################
# # 4. Дан список my_list в котором могум быть как строки так и целые числа.
# # Создать новый список в который поместить только строки из my_list.
# #
# my_list = ["Apple", 5, "Pear", 1, "Apricot", 3, "Ginger", 1, "Avocado", 1, "Orange", 2]
# # my_list_1 = [item for item in my_list if not str(item).isdigit()]
# my_list_1 = [item for item in my_list if str(item).isalpha()]
# print(my_list_1)
# print(my_list)



####################################
# # # 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# # # которые встречаются в строке только один раз.
# # #
# # my_str = "создать список"
# # my_list = []
# # my_list_2 = [my_list.append(symbol) for symbol in my_str if symbol not in my_list]
# # print(my_list)
# #
# my_str = "создать список"
# my_list = list(set(my_str))
# print(my_list)



####################################
# # 6. Даны две строки. Создать список в который поместить те символы,
# # которые есть в обеих строках хотя бы раз.
#
# my_str_1 = "создать список"
# my_str_2 = "создать две строки "
#
# # my_str_1 = set(my_str_1)
# # my_str_2 = set(my_str_2)
# # print(my_str_1)
# # print(my_str_2)
# # my_str = my_str_1.intersection(my_str_2)
# my_str = list(set(my_str_1).intersection(set(my_str_2)))
# print(my_str)


####################################
# # 7. Даны две строки. Создать список в который поместить те символы,
# # которые есть в обеих строках, но в каждой только по одному разу.
#
# my_str_1 = "создать список"
# my_str_2 = "создать две строки "
#
# my_1 = set([symbol for symbol in my_str_1 if my_str_1.count(symbol) == 1])
# my_2 = set([symbol for symbol in my_str_2 if my_str_2.count(symbol) == 1])
# print(my_1)
# print(my_2)
# result = list(my_1.intersection(my_2))
# print(result)


