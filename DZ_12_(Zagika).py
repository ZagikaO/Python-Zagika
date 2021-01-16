import re
import requests
import json
import csv
import random

# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).


def get_quote() -> dict:
    """Return quote from www"""
    url = "http://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "format": "json",
              "key": random.randint(3, 100),
              "lang": "ru"}
    r = requests.get(url, params=params)
    quote = r.json()
    return quote
# print(get_quote())


def create_quote_list(count_quote=15) -> list:
    """Create list with quotes"""
    quote_list = []
    while len(quote_list) != count_quote:
        quote = get_quote()
        if quote["quoteAuthor"] != "":
            quote_list.append([quote["quoteAuthor"], quote["quoteText"], quote["quoteLink"]])
    return quote_list


quote_list = create_quote_list()
# print(quote_list)


def sort_by_author(quote_list: list) -> str:
    for line in quote_list:
        author = line[0]
        return author


sorted_by_Author = sorted(quote_list, key=sort_by_author)


def update_list_fieldnames() -> list:
    """Create list quotes with fieldnames"""
    fieldnames = [["Author", "Quote", 'URL']]
    for line in sorted_by_Author:
        fieldnames.append(line)
    return fieldnames


def create_csv_file_with_quotes():
    """Create csv file with result - list quotes and fieldnames"""
    with open("quotes.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(update_list_fieldnames())


create_csv_file_with_quotes()


# 2. Дан файл authors.txt

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
# print(authors)

# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
#
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]


def find_dates() -> list:
    """Separate date"""
    list_dates = []
    for item in authors:
        list_dates.append(re.split(" - |,|'", item)[0])
    return list_dates


def find_names() -> list:
    """Separate name"""
    list_names = []
    for item in authors:
        list_names.append(re.split(" - |,|'|- ", item)[1])
    return list_names


calendar_dict = {"January": "/01/",
                 "February": "/02/",
                 "March": "/03/",
                 "April": "/04/",
                 "May": "/05/",
                 "June": "/06/",
                 "July": "/07/",
                 "August": "/08/",
                 "September": "/09/",
                 "October": "/10/",
                 "November": "/11/",
                 "December": "/12/"}


def group_for_dates() -> list:
    """Separate day, month, year"""
    list_group_dates = []
    for item in dates:
        list_group_dates.append(re.split(" ", item))
    return list_group_dates


def change_format_for_month(calendar_dict: dict) -> list:
    """Change name month to format from dictionary"""
    for key in calendar_dict:
        for lists in group_dates:
            if lists[1] == key:
                lists[1] = calendar_dict[lists[1]]
    return group_dates


def change_format_for_day() -> list:
    """Change days to required format"""
    for lists in dates_with_month:
        lists[0] = re.findall(r"[0-9]+", lists[0])
        lists[0] = "".join(lists[0])
    return dates_with_month


def create_modified_date() -> list:
    """Change full date to required format"""
    date_lists = []
    for lists in dates_with_days:
        lists = "".join(lists)
        date_lists.append(lists)
    return date_lists


def create_dict_names() -> list:
    """Create dictionary with names"""
    dict_names = [{"name:": value} for value in names]
    return dict_names


def create_dict_dates() -> list:
    """Create dictionary with dates"""
    dict_dates = [{"date:": value} for value in modified_date]
    return dict_dates


def create_dict_authors() -> list:
    """Unit dictionary with dates and names"""
    dict_authors = []
    for item in range(len(dict_names)):
        dict_authors.append({**dict_names[item], **dict_dates[item]})
    return dict_authors


names = find_names()
dates = find_dates()
group_dates = group_for_dates()
dates_with_month = change_format_for_month(calendar_dict=calendar_dict)
dates_with_days = change_format_for_day()
modified_date = create_modified_date()
dict_names = create_dict_names()
dict_dates = create_dict_dates()
dict_authors = create_dict_authors()
print(dict_authors)


# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.

def save_json_file():
    """Save dictionary authors to json file"""
    with open("authors.json", "w") as file:
        json.dump(dict_authors, file, indent=2)


save_json_file()


# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).


# DictWriter


def get_dict_quote() -> dict:
    """Return quote from www"""
    url2 = "http://api.forismatic.com/api/1.0/"
    params2 = {"method": "getQuote",
              "format": "json",
              "key": random.randint(3, 100),
              "lang": "ru"}
    r2 = requests.get(url2, params=params2)
    quote2 = r2.json()
    return quote2


# dict_quote = get_dict_quote()
# print(get_dict_quote())


def create_dict_list(count_quote2=7) -> list:
    """Create list with different quotes as dict"""
    list_dict_quotes = []
    while len(list_dict_quotes) != count_quote2:
        quote2 = get_dict_quote()
        if quote2["quoteAuthor"] != "":
            list_dict_quotes.append(quote2)
    return list_dict_quotes


# list_dict_quotes = create_dict_list()
# print(create_dict_list())


def create_list_with_fieldnames() -> list:
    """Create list with needed correct fieldnames"""
    dict_fieldnames = []
    for dict in create_dict_list():
        dict_fieldnames.append({"Author": dict["quoteAuthor"], "Quote": dict["quoteText"], "URL": dict["quoteLink"]})
    return dict_fieldnames


# list_new_fieldnames = create_list_with_fieldnames()
# print(list_new_fieldnames)


def sort_dict_quotes(list_new_fieldnames: list) -> list:
    author2 = list_new_fieldnames["Author"]
    return author2


sort_dict_quotes = sorted(create_list_with_fieldnames(), key=sort_dict_quotes)


def _create_csv_file2():
    """Create csv file with result - list quotes and fieldnames"""
    with open("quotes2.csv", "w", encoding='utf-8') as csv_file:
        fieldnames = ["Author", "Quote", "URL"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sort_dict_quotes)


_create_csv_file2()