import re
import requests
import json
import csv
import random
# quote_text = quote["quoteText"]
# quote_author = quote["quoteAuthor"]
# quote_url = quote["quoteLink"]
# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).


def get_quote():
    url = "http://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "format": "json",
              "key": random.randint(2, 100),
              "lang": "ru"}
    r = requests.get(url, params=params)
    quote = r.json()
    return quote


def create_quote_list(count_quote=15) -> list:
    quote_list = []
    for item in range(count_quote):
        quote = get_quote()
        if quote["quoteAuthor"] != "":
            quote_list.append([quote["quoteAuthor"], quote["quoteText"], quote["quoteLink"]])
    return quote_list


quote_list = create_quote_list()
print(quote_list)


def sort_by_author(quote_list: list) -> list:
    for line in quote_list:
        author = line[0]
        return author


sorted_by_Author = sorted(quote_list, key=sort_by_author)


def update_list_fieldnames():
    """Create list"""
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


# # 2. Дан файл authors.txt
#
# # 2.1) написать функцию, которая считывает данные из этого файла,
# # возвращая список строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# # Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.
#
#
# def read_file_authors(filename: str) -> list:
#     with open(filename, "r") as file:
#         data = []
#         for line in file.readlines():
#             data.append(line.strip())
#     return [item for item in data if ("birthday" or "death") in item]
#
#
# filename = "authors.txt"
# authors = read_file_authors(filename=filename)
# print(authors)
#
# # 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# # в формате {"name": name, "date": date},
# # где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# #
# # Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# # {"name": "J. D. Salinger", "date": "01/01/1919"}]
#
#
# def find_dates() -> list:
#     """Separate date"""
#     list_dates = []
#     for item in authors:
#         list_dates.append(re.split(" - |,|'", item)[0])
#     return list_dates
#
#
# def find_names() -> list:
#     """Separate name"""
#     list_names = []
#     for item in authors:
#         list_names.append(re.split(" - |,|'|- ", item)[1])
#     return list_names
#
#
# calendar_dict = {"January": "/01/",
#                  "February": "/02/",
#                  "March": "/03/",
#                  "April": "/04/",
#                  "May": "/05/",
#                  "June": "/06/",
#                  "July": "/07/",
#                  "August": "/08/",
#                  "September": "/09/",
#                  "October": "/10/",
#                  "November": "/11/",
#                  "December": "/12/"}
#
#
# def group_for_dates() -> list:
#     """Separate day, month, year"""
#     list_group_dates = []
#     for item in dates:
#         list_group_dates.append(re.split(" ", item))
#     return list_group_dates
#
#
# def change_format_for_month(calendar_dict: dict) -> list:
#     """Change name month to format from dictionary"""
#     for key in calendar_dict:
#         for lists in group_dates:
#             if lists[1] == key:
#                 lists[1] = calendar_dict[lists[1]]
#     return group_dates
#
#
# def change_format_for_day() -> list:
#     """Change days to required format"""
#     for lists in dates_with_month:
#         lists[0] = re.findall(r"[0-9]+", lists[0])
#         lists[0] = "".join(lists[0])
#     return dates_with_month
#
#
# def create_modified_date() -> list:
#     """Change full date to required format"""
#     date_lists = []
#     for lists in dates_with_days:
#         lists = "".join(lists)
#         date_lists.append(lists)
#     return date_lists
#
#
# def create_dict_names() -> list:
#     """Create dictionary with names"""
#     dict_names = [{"name:": value} for value in names]
#     return dict_names
#
#
# def create_dict_dates() -> list:
#     """Create dictionary with dates"""
#     dict_dates = [{"date:": value} for value in modified_date]
#     return dict_dates
#
#
# def create_dict_authors() -> list:
#     """Unit dictionary with dates and names"""
#     dict_authors = []
#     for item in range(len(dict_names)):
#         dict_authors.append({**dict_names[item], **dict_dates[item]})
#     return dict_authors
#
#
# names = find_names()
# dates = find_dates()
# group_dates = group_for_dates()
# dates_with_month = change_format_for_month(calendar_dict=calendar_dict)
# dates_with_days = change_format_for_day()
# modified_date = create_modified_date()
# dict_names = create_dict_names()
# dict_dates = create_dict_dates()
# dict_authors = create_dict_authors()
# print(dict_authors)
#
#
# # 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.
#
# def save_json_file():
#     """Save dictionary authors to json file"""
#     with open("authors.json", "w") as file:
#         json.dump(dict_authors, file, indent=2)
#
#
# save_json_file()