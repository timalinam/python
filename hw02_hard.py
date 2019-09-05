# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

crop = (equation.split(' = ', maxsplit=-1))[1]
k = int((crop.split('x ', maxsplit=-1))[0])

if '-' in (crop.split('x ', maxsplit=-1))[1]:
    b = -float((crop.split(' ', maxsplit=-1))[2])
else:
    b = float((crop.split(' ', maxsplit=-1))[2])

y = k*x + b

print('{}, если x = {}: y = {}'.format(equation, x, y))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

import re

user_date = input("Введите дату:\n")
correct = False
rex = re.compile("^[0-3][0-9][.][0-1][0-9][.][0-9]{4}$")
if rex.match(user_date):
    user_date_list = [int(i) for i in user_date.split('.', maxsplit=-1)]

    day = user_date_list[0]
    month = user_date_list[1]
    year = user_date_list[2]

    if 0 < month <= 7 and month % 2 == 0 and 1 < day <= 30:
        correct = True
    elif 0 < month <= 7 and month % 2 == 1 and 1 < day <= 31:
        correct = True
    elif 7 < month <= 12 and month % 2 == 1 and 1 < day <= 30:
        correct = True
    elif 7 < month <= 12 and month % 2 == 0 and 1 < day <= 31:
        correct = True

if correct:
    print("Дата введена верно")
else:
    print("Дата введена неверно")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

room = int(input('Введите номер комнаты\n'))

room_right_square = 0  # Номер последней комнаты в квадрате
room_right_pr = 0  # Номер последней комнаты в предыдущем квадрате
flr_lst_room = 0  # Номер этажа последней комнаты в квадрате
number_square=0  # Номер квадрата из комнат

# Вычислим значения указанные выше

while room_right_square < room:
    room_right_pr = room_right_square
    room_right_square += number_square**2
    flr_lst_room += number_square
    number_square += 1

number_square -= 1

# Вычислим номер этажа на котором находится искомая комната

room_right = room_right_square
floor = flr_lst_room

while room_right >= room:
    floor -=1
    room_right -= number_square
floor += 1

# Вычислим порядковый номер комнаты на этаже

if (room - room_right_pr) % number_square == 0:
    number_room = number_square
else:
    number_room = (room - room_right_pr) % number_square

print('Комната находится на {} этаже и ее номер слева: {}'.format(floor,number_room))






