import random
import string

# Цель задания - создать функции, которые будут генерировать случайные данные нужного формата
# для записи в файлы разных типов.
#
# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.

def generate_string(min_limit=100, max_limit=1000) -> str:
    str_len = random.randint(min_limit, max_limit)
    res_list = [chr(random.randint(ord('a'), ord('z'))) for _ in range(str_len)]
    return ''.join(res_list)

def transformation_with_spaces(str_to_transform):
    count_spaces = len(str_to_transform) // 5
    spaces_indexes = []
    while len(spaces_indexes) < count_spaces:
        index = random.randint(5, len(str_to_transform) - 5)
        if index not in spaces_indexes:
            spaces_indexes.append(index)
    for index in spaces_indexes:
        str_to_transform = str_to_transform[:index] + " " + str_to_transform[index + 1:]
    return str_to_transform

def change_first_symbol(word):
    return word.capitalize()

def change_last_symbol(word):
    puntcuations = ",.!?"
    word = word[:-1] + random.choice(puntcuations) if len(word) > 3 else word
    return word

def change_word_to_number(word):
    if len(word) <= 3:
        number_list = [str(random.randint(0, 9)) for _ in range(len(word))]
        word = "".join(number_list)
    return word

def random_word_transformation(word):
    state = random.randint(1, 5)
    if state == 1:
        word = change_first_symbol(word)
    elif state == 2:
        word = change_last_symbol(word)
    elif state == 3:
        word = change_word_to_number(word)
    return word

def transform_by_words(str_to_transform):
    words = str_to_transform.split()
    new_words = []
    for word in words:
        new_word = random_word_transformation(word)
        new_words.append(new_word)
    return " ".join(new_words)

def transformation_with_line(str_to_transform):
    count_spaces = len(str_to_transform) // 100
    spaces_indexes = []
    while len(spaces_indexes) < count_spaces:
        index = random.randint(5, len(str_to_transform) - 5)
        if index not in spaces_indexes:
            spaces_indexes.append(index)
    for index in spaces_indexes:
        str_to_transform = str_to_transform[:index] + "\n" + str_to_transform[index + 1:]
    return str_to_transform

result = generate_string()
result = transformation_with_spaces(result)
result = transform_by_words(result)
result = transformation_with_line(result)
print(result)

# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.



# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.
#
# А теперь основное задание:
# Написать функцию generate_and_write_file которая принимает один параметр - имя файла(вместе с путем).
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"