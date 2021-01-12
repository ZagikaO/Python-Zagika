# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

# import requests
#
# url = "http://api.forismatic.com/api/1.0/"
# params = {"method": "getQuote",
#           "format": "json",
#           "key": 1,
#           "lang": "ru"}
# r = requests.get(url, params=params)
# quote = r.json()
# quote_text = quote["quoteText"]
# quote_author = quote["quoteAuthor"]
# print(quote)
#
# # def get_quote(count = 10):
# new_list = [x for x in range(10)]



# 2. Дан файл authors.txt
#
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая список строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.

def read_file_authors(filename: str) -> list:
    with open(filename, "r") as file:
        data = []
        for line in file.readlines():
            data.append(line.strip())
    return [item for item in data if ("birthday" or "death") in item]

filename = "authors.txt"
authors = read_file_authors(filename=filename)
print(authors)

# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
#
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]
# import json
import re

list_test = []
for item in authors:
    list_test.append(re.split(' - |,', item)[0:2])
print(list_test)

# my_item = ['1st January 1919', "J. D. Salinger's birthday"]
dict_keys = ["name", "date"]

# my_dict = {item: my_item for item in dict_keys}

print(my_dict)


# def create_dict_authors():


# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.