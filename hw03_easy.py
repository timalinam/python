# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number_int = number*(10**(ndigits+1))
    number_int_fract = number*(10**(ndigits+1))%1
    number_int = number_int - number_int_fract
    last_number = number_int%10
    number_int = number_int/10 - last_number/10
    if last_number > 5:
        number_int = number_int + 1
    number_float = number_int/(10**ndigits)
    return number_float

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    list_number = list(str(ticket_number))
    sum1 = 0
    sum2 = 0
    center = round((len(list_number)/2)+0.1)
    for i in range(0, center):
        sum1 += int(list_number[i])
    if not len(list_number)%2 == 0:
        center = center - 1
    for i in range(center, len(list_number)):
        sum2 += int(list_number[i])
    if sum1 == sum2:
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))