
__author__ = 'Хохлова Марина Михайловна'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

number = input('Введите целое число\n')

i = 0

print('Вывод цифр исходного числа через цикл while:')
while i < len(number):
    print(number[i])
    i += 1

print('Вывод цифр исходного числа через цикл for:')
for num in number:
    print(num)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input('Введите значение переменной 1\n')
b = input('Введите значение переменной 2\n')

print('Меняю местами...')

m = a
a = b
b = m

print('Переменная 1 =', a)
print('Переменная 2 =', b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Введите свой возраст\n'))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')