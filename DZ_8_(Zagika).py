from random import randint, choice
import string
# import random

# 1. Написать функцию, которая считывает из файла domains.txt
# названия некоторых интернет доменов и возвращает их в виде списка строк (названия возвращать без точки).
def create_list_domains(openfile_domains: str, read_from: int, result_domains: list):
    """Create list with domains"""
    with open(openfile_domains, "r") as file:
        for line in file.readlines():
            result_domains.append(line[(read_from)::].strip())
    return result_domains

openfile_domains = "domains.txt"
read_from = 1
result_domains = []

list_domains = create_list_domains(openfile_domains=openfile_domains,
                                   read_from=read_from,
                                   result_domains=result_domains)
print("1) return list_domains for my function: ", list_domains)

# 2. Написать функцию, которая считывает данные из файла names.txt
# и возвращает список всех фамилий из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии)
def create_list_names(openfile_name: str, count_item: int, result_names: list):
    """Create list with lastnames"""
    with open(openfile_name, "r") as file:
        for line in file.readlines():
            result_names.append(line.split("\t")[count_item])
    return result_names

openfile_name = "names.txt"
count_item = 1
result_names = []

list_names = create_list_names(openfile_name=openfile_name,
                               count_item=count_item,
                               result_names=result_names)
print("2) return list_names for my function: ", list_names)

# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2.
# Строку и число генерировать случайным образом. Буквы могут повторяться.
# Пример: miller.249@sgdyyur.com

def create_mails(list_names: list, string_site: str):
    mails = str(choice(list_names)) + "." + str(randint(100, 999)) + "@" + string_site + str(choice(create_list_domains(openfile_domains, 0, [])))
    return mails

string_site = ''.join(choice(string.ascii_lowercase) for _ in range(randint(5, 7)))
mails = create_mails(list_names, string_site)
print("3) return mail: ", mails)

