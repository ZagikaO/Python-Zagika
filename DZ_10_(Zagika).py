import json
import re
import string

############################################################
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
def read_file(reading_file: str):
    with open(reading_file, "r", encoding='utf-8') as file:
        return json.load(file)
reading_file = "data.json"
mathematician = read_file(reading_file)
print(mathematician)

# ############################################################
# # 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# # Например для Rene Descartes фамилия это Desca
# rtes, у Pierre de Fermat - Fermat и т.д.
# # Если фамилии нет, то использовать имя, например Euclid.
def sort_by_name(line: dict) -> str:
    name = line["name"].split()[-1]
    return name

sorted_file_by_name = sorted(mathematician, key=sort_by_name)
print(sorted_file_by_name)

############################################################
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
def sort_by_date(line: dict) -> int:
    years = re.findall(r"[0-9]+", line["years"])
    years = int(years[1])
    if "BC" in line["years"]:
        years = years * (-1)
    return years

sorted_file_by_date = sorted(mathematician, key=sort_by_date)
print(sorted_file_by_date)

# ############################################################
# # 4. Написать функцию сортировки по количеству слов в поле "text"
def sort_by_len_text(line: dict) -> int:
    text = "".join(re.findall(r"[string.ascii_lowercase, string.ascii_uppercase]", line["text"]))
    text = text.split()
    return len(text)

sorted_file_by_text = sorted(mathematician, key=sort_by_len_text)
print(sorted_file_by_text)