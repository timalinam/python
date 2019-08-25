# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def identfy_sign(user_string):
    crop_lst = user_string.split(' ')
    if '-' in crop_lst:
        return '-', user_string.split(' - ')
    else:
        return '+', user_string.split(' + ')

def identify_numbers(crop_str):
    if ' ' in crop_str:
        crop_lst = crop_str.split(' ')
        n = int(crop_lst[0])
        fract_lst = crop_lst[1].split('/')
        x = int(fract_lst[0])
        y = int(fract_lst[1])
    elif '/' in crop_str:
        n = 0
        crop_lst = crop_str.split('/')
        x = int(crop_lst[0])
        y = int(crop_lst[1])
    else:
        n = 0
        x = int(crop_str)
        y = 1

    if n*x*y > 0:
        n = abs(n)
        x = abs(x)
        y = abs(y)
    elif n*x*y < 0:
        n = -abs(n)
        x = abs(x)
        y = abs(y)
    return n, x, y

def sum_numbers(n1, x1, y1, n2, x2, y2, sign):

    def max_del(a,b):
        md = 1
        for i in range(1, a+1):
            if a%i == 0 and b%i == 0:
                md = i
        return md

    def improper_fraction(n, x, y):
        if n < 0:
            x = -(abs(n)*y + x)
        else:
            x = n*y + x
        return x

    x1 = x1 * y2
    x2 = x2 * y1
    y = y1 * y2
    x1 = improper_fraction(n1, x1, y)
    x2 = improper_fraction(n2, x2, y)
    if sign == '+':
        x = x1 + x2
    else:
        x = x1 - x2

    n = x//y
    x = x % y

    md = max_del(x, y)
    x = x/md
    y = y/md

    return n, x, y

user_string = input('Введите выражение для вычисления\n')
sign, crop_user_string = identfy_sign(user_string)
fract1 = crop_user_string[0]
fract2 = crop_user_string[1]
n1, x1, y1 = identify_numbers(fract1)
n2, x2, y2 = identify_numbers(fract2)
n, x, y = sum_numbers(n1, x1, y1, n2, x2, y2, sign)

if n == 0:
    print(f'{int(x)}/{int(y)}')
elif x == 0:
    print(f'{int(n)}')
else:
    print(f'{int(n)} {int(x)}/{int(y)}')



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))