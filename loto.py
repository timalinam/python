#!/usr/bin/python3
import random

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""


class Loto1:
    def __init__(self):
        self.name = self

    loto_numbers = [i for i in range(1, 91)]

    def take_keg(self):
        keg_number = self.loto_numbers.pop(self.loto_numbers.index(random.choice(self.loto_numbers)))
        print(f'Новый бочонок: {keg_number} (осталось {len(self.loto_numbers)})')
        return keg_number

    def check_number(self, keg_number, line2, line3, line4):
        if keg_number in line2:
            i = line2.index(keg_number)
            line2[i] = '--'
            return line2, line3, line4, True
        elif keg_number in line3:
            i = line3.index(keg_number)
            line3[i] = '--'
            return line2, line3, line4, True
        elif keg_number in line4:
            i = line4.index(keg_number)
            line4[i] = '--'
            return line2, line3, line4, True
        else:
            return line2, line3, line4, False

    def game_over(self, line2, line3, line4):
        line = line4 + line2 + line3
        a = True
        for itm in line:
            if type(itm) == int:
                a = False
                break
        return a


class Card(Loto1):
    loto_numbers1 = [i for i in range(1, 91)]

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.line2, self.line3, self.line4 = self.generate_lines()
        self.str1, self.str2, self.str3, self.str4, self.str5 = self.generate_str(self.name, self.line2, self.line3,
                                                                                  self.line4)

    def __str__(self):
        return f'{self.str1}\n{self.str2}\n{self.str3}\n{self.str4}\n{self.str5}\n'

    def generate_lines(self):

        card_numbers = [self.loto_numbers1.pop(self.loto_numbers1.index(random.choice(self.loto_numbers1))) for i in
                        range(15)]

        def generate_line():
            line = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
            positions = random.sample(range(9), 5)
            num_for_line = sorted([card_numbers.pop(card_numbers.index(random.choice(card_numbers))) for i in range(5)])
            n = 0
            for i in range(9):
                if i in positions:
                    line[i] = num_for_line[n]
                    n += 1
            return line

        list_str2 = generate_line()
        list_str3 = generate_line()
        list_str4 = generate_line()

        return list_str2, list_str3, list_str4

    def generate_str(self, name, list_str2, list_str3, list_str4):
        if self.name == 'компьютер':
            str1 = '------ Карточка компьютера --------'
        else:
            str1 = '--------- Ваша карточка -----------'
        str5 = '-' * 35

        str2 = f'{list_str2[0]:>2}  {list_str2[1]:>2}  {list_str2[2]:>2}  {list_str2[3]:>2}  {list_str2[4]:>2}  {list_str2[5]:>2}  {list_str2[6]:>2}  {list_str2[7]:>2}  {list_str2[8]:>2}'
        str3 = f'{list_str3[0]:>2}  {list_str3[1]:>2}  {list_str3[2]:>2}  {list_str3[3]:>2}  {list_str3[4]:>2}  {list_str3[5]:>2}  {list_str3[6]:>2}  {list_str3[7]:>2}  {list_str3[8]:>2}'
        str4 = f'{list_str4[0]:>2}  {list_str4[1]:>2}  {list_str4[2]:>2}  {list_str4[3]:>2}  {list_str4[4]:>2}  {list_str4[5]:>2}  {list_str4[6]:>2}  {list_str4[7]:>2}  {list_str4[8]:>2}'

        return str1, str2, str3, str4, str5


if __name__ == '__main__':
    card_pc = Card('компьютер')
    card_user = Card('Марина')
    print(card_pc)
    print(card_user)
    while True:
        game = Loto1()
        if game.game_over(card_user.line2, card_user.line3,card_user.line4):
            print(f'Игра окончена, победил {card_user.name}')
            break
        elif game.game_over(card_pc.line2, card_pc.line3,card_pc.line4):
            print(f'Игра окончена, победил {card_pc.name}')
            break
        keg_number = game.take_keg()

        answer = ' '

        while answer not in "yn":
            answer = input('Вычеркнуть?(y/n)\n')

        if answer == 'y':
            card_user.line2, card_user.line3, card_user.line4, number_in_card = game.check_number(keg_number,
                                                                                                  card_user.line2,
                                                                                                  card_user.line3,
                                                                                                  card_user.line4)
            if not number_in_card:
                print('Вы проиграли. Такого числа на Вашей карточке нет')
                break
        elif answer == 'n':
            card_user.line2, card_user.line3, card_user.line4, number_in_card = game.check_number(keg_number,
                                                                                                  card_user.line2,
                                                                                                  card_user.line3,
                                                                                                  card_user.line4)
            if number_in_card:
                print('Вы проиграли. Вы не вычеркнули имеющееся число')
                break

        card_pc.line2, card_pc.line3, card_pc.line4, number_in_card = game.check_number(keg_number, card_pc.line2,
                                                                                        card_pc.line3, card_pc.line4)

        card_pc.str1, card_pc.str2, card_pc.str3, card_pc.str4, card_pc.str5 = card_pc.generate_str('компьютер', card_pc.line2, card_pc.line3, card_pc.line4)
        card_user.str1, card_user.str2, card_user.str3, card_user.str4, card_user.str5 = card_user.generate_str('Марина', card_user.line2, card_user.line3, card_user.line4)

        print(card_pc)
        print(card_user)
