'''
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия
столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
'''
import csv
import re
import chardet


def get_data():

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []
    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as file:
            data_bytes = file.read()
            coding = chardet.detect(data_bytes)  # определяю кодировку
            data = data_bytes.decode(coding['encoding'])

        # забираю информацию о производителе
        prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(prod_reg.findall(data)[0].split()[2])

        # Операционная система
        name_reg = re.compile(r'Windows\s*\S*')
        os_name_list.append(name_reg.findall(data)[0])

        # Код продукта
        code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(code_reg.findall(data)[0].split()[2])

        # Тип системы
        type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(type_reg.findall(data)[0].split()[2])

    headers = ['Изготовитель систем', 'OC', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    data_rows = [os_prod_list, os_name_list, os_code_list, os_type_list]
    for idx in range(len(data_rows[0])):
        line = [row[idx] for row in data_rows]
        main_data.append(line)
    return main_data

def write_to_csv(out_file):
    data = get_data()
    with open(out_file, 'w', encoding='utf-8') as f:
        csv.writer(f, delimiter=',').writerows(data)
    print('Finish')

if __name__ == '__main__':
    write_to_csv('result.csv')
