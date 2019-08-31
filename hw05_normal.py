# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import hw05_easy
import os
import main

def menu():
    menu_items = {
        '1': ('Перейти в папку', change_dir, 'Введите путь к папке,в которую хотите перейти\n'),
        '2': ('Посмотреть содержимое текущей папки', print_content, None),
        '3': ('Удалить папку', hw05_easy.dell_folders, 'Введите название папки, которую хотите удалить\n'),
        '4': ('Cоздать папку', hw05_easy.add_folders, 'Введите название папки, которую хотите создать\n'),
        'exit': ('Завершить программу', main.break_game, None),
    }
    print('Главное меню')
    for key, value in menu_items.items():
        print(f'{key} - {value[0]}')
    print('#' * 10)

    while True:
        ask = input('Что выбираем?\n')
        if ask.lower() in menu_items:
            return menu_items[ask.lower()][1], menu_items[ask.lower()][2]
        else:
            print('Неверный ввод, проверьте правильность ввода.')

def change_dir(path):
    try:
        os.chdir(path)
        print('Успешно перешел в папку')
    except OSError:
        print('Не удалось перейти в папку')

def print_content():
    try:
        print(os.listdir(os.getcwd()))
    except OSError:
        print('Не удалось отобразить содержимое')

if __name__ == '__main__':
    while True:
        start, text = menu()
        if text is None:
            start()
        else:
            start(input(text))


