# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib1 = 1
    fib2 = 1
    fib = [1, 1]
    for i in range(0, m - 2):
        fib2, fib1 = fib1 + fib2, fib2
        fib.append(fib2)
    return fib[n - 1:m]


print(fibonacci(3, 11))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(len(origin_list) - 1 - i):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filt(func, orig_list):
    for i in orig_list[:]:

        if not func(i):
            orig_list.remove(i)
    return orig_list


print(filt(lambda x: x.isdigit(), ['5', 'ghgsh', '76', '333', 'sdfga', 'ddd', 'ssasa']))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram_check(x1, y1, x2, y2, x3, y3, x4, y4):
    if abs(x1 - x2) == abs(x3 - x4) and abs(y1 - y2) == abs(y3 - y4):
        return True
    else:
        return False

x1 = -1
y1 = -5
x2 = -1
y2 = -2
x3 = 1
y3 = -2
x4 = 1
y4 = -5

print(parallelogram_check(x1, y1, x2, y2, x3, y3, x4, y4))
