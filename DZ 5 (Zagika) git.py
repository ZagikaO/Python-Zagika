# 1. Дано целое число (int). Определить сколько нулей в этом числе.

value = int(215650654608450)
value = str(value)
count = value.count("0")
print(count)

###########################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.

value = int(21565065460845)
value_1 = int(str(value)[::-1])
count_null = len(str(value))-len(str(value_1))
print(count_null)

###########################
# 3. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
my_result = []
for symbol_1 in my_list_1[1::2]:
    my_result.append(symbol_1)
for symbol_1 in my_list_2[1::2]:
    my_result.append(symbol_1)
print(my_result)

###########################
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
new_list.append(my_list[0])
del new_list[0]
print(new_list)

###########################
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 2, 3, 4, 5]
my_list.append(my_list[0])
my_list.pop(0)
print(my_list)

###########################
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.

my_str = "43 больше чем 34 но меньше чем 56"
res = ""
for symbol in my_str:
    if symbol.isdigit() or symbol.isspace( ):
        res += symbol
# print(res)
new_result = res.split(" ")
while "" in new_result:
    new_result.remove("")
# print(new_result)
res_1 = []
for symbol in new_result:
    symbol = int(symbol)
    res_1.append(symbol)
# print(res_1)
res_2 = sum(res_1)
print(res_2)

###########################
# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']

my_str = "43 больше чем 34 но меньше чем 56"
# print(len(my_str))
my_list_even = []
my_list_odd = []
my_result = []
for index, value in enumerate(my_str):
    if not index % 2:
        my_list_odd.append(value)
    else:
        my_list_even.append(value)
if len(my_list_odd) == len(my_list_even):
    for index in range(len(my_list_odd)):
        my_result.append(my_list_odd[index] + my_list_even[index])
else:
    odd_pop = my_list_odd.pop() + "_"
    for index in range(len(my_list_odd)):
        my_result.append(my_list_odd[index] + my_list_even[index])
    my_result.append(odd_pop)
# print(len(my_str))
# print(len(my_list_even))
# print(len(my_list_odd))
print(my_result)

#############################
# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
#
my_str = "My_long str"
l_limit = "o"
r_limit = "t"
# index_l = my_str.index(l_limit)
# index_r = my_str.index(r_limit)
# # print(index_l)
# # print(index_r)
result = my_str[my_str.index(l_limit) + 1:my_str.index(r_limit)]
print(result)

# ###########################
# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long stringhgjhhgfdd"
l_limit = "o"
r_limit = "g"
my_str_1 = my_str[::-1]
# print(my_str)
# print(my_str_1)
index_l = my_str.index(l_limit)
index_r = my_str_1.index(r_limit)
# print(index_l)
# print(index_r)
result = my_str[index_l + 1:(index_r + 1) * -1]
print(result)

###########################
# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2,4,1,5,3,9,0,7]
my_list_2 = []
my_result = []
for index, value in enumerate(my_list):
    if index > 0 and index < len(my_list)-1:
        my_list_2.append(value)
for index, value in enumerate(my_list_2):
    if my_list_2[index] > my_list[index]+my_list[index+2]:
        my_result.append(value)
# print(my_list)
# print(my_list_2)
print(my_result)
print(len(my_result))