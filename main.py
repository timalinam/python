import random

exit_str = 'Для выхода введите exit'

gamer = {'name': {'question': 'Как тебя зовут?',
                  'param': {'type': 'str'},
                  'answer': None},
         'age': {'question': 'Сколько тебе лет?',
                 'param': {'type': int,
                           'error_msg': 'Введите число полных лет '},
                 'answer': None},
         'sex': {'question': 'Введите ваш пол (м/ж)',
                 'param': {'type': str,
                           'good': ('м', 'ж'),
                           'error_msg': 'Пол нужно вводить м или ж'},
                 'answer': None},
         'pet_name': {'question': 'Как зовут вашего питомца?',
                      'param': {'type': 'str'},
                      'answer': None},
         'love_game': {'question': 'Любите ли вы играть (да/нет)',
                       'param': {'type': bool,
                                 'good': ('да', 'нет'),
                                 'compliance': {'да': True, 'нет': False},
                                 'error_msg': 'Нужно ввести да или нет'
                                 },
                       'answer': None},
         }


def break_game():
    print('Пока! Жду тебя снова')
    exit()


def error_print(**kwargs):
    print(kwargs['param']['error_msg'])


def register_user(**kwargs):
    for key, item in kwargs.items():
        while True:
            ask = input(item['question'] + '\n')
            if ask.lower() == 'exit':
                break_game()
            else:
                if item.get('param').get('good') and (ask.lower() not in item.get('param').get('good')):
                    error_print(**item)
                    continue
                elif item.get('param').get('type') is int:
                    if not ask.isdigit():
                        error_print(**item)
                        continue
                    else:
                        ask = int(ask)
                elif item.get('param').get('type') is bool:
                    ask = item['param']['compliance'][ask]
            item['answer'] = ask
            break
def game_rock_paper_scissors():
    game_strict = {'question': 'Бросай свой предмет (Камень, Ножницы, Бумага)',
                   'param': {'type': str,
                            'good': ('камень','ножницы','бумага'),
                            'error_msg': 'Такого предмета нет, введи правильно!',
                            },
        'results': {gamer['name']['answer']: 0, 'computer': 0, 'dead_heat': 0},
        'game_step': 0
    }

    while True:
        game_strict['game_step'] += 1
        comp = random.choice(game_strict['param']['good'])
        ask = input(game_strict['question'] + '\n')
        len_name = len(gamer['name']['answer'])

        if ask.lower() == 'exit':
            break_game()
        elif ask.lower() == 'menu':
            break

        if ask.lower() not in game_strict['param']['good']:
            error_print(**game_strict)
        elif ask.lower() == comp:
            game_strict['results']['dead_heat'] += 1
        elif (ask.lower() == 'бумага' and comp == 'камень') or (ask.lower() == 'камень' and comp == 'ножницы') or (ask.lower() == 'ножницы' and comp == 'бумага'):
            game_strict['results'][gamer['name']['answer']] += 1
        else:
            game_strict['results']['computer'] += 1

        stat_info = {
            'title': f'''xoд: {game_strict['game_step']}''',
            'names': f'''{gamer['name']['answer'].title().center(len_name)} # {'computer'.title().center(len_name)}''',
            'score': f'''{str(game_strict['results'][gamer['name']['answer']]).center(len_name)}#{str(game_strict['results']['computer']).center(len_name)}''',
            'footer': f'''Ничьи: {game_strict['results']['dead_heat']}'''
        }

        print('#'.center(len_name))
        for key, values in stat_info.items():
            print(values.center(len_name, '#'))


def menu():
    menu_items = {
        '1': ('Каких букв нет в моем имени', game_not_in_alphabet),
        '2': ('Угадай где число', game_where_number),
        '3': ('Камень, Ножницы, Бумага', game_rock_paper_scissors),
        'exit': ('Завершить программу', break_game),
    }
    print('Главное меню')
    for key, value in menu_items.items():
        print(f'{key} - {value[0]}')
    print('#' * 10)

    while True:
        ask = input('Что выбираем?\n')
        if ask.lower() in menu_items:
            return menu_items[ask.lower()][1]
        else:
            error_print(param = {'error_msg': 'Неверный ввод, проверьте правильность ввода.'})
def check_age():
    if  gamer['age']['answer'] < 18:
        error_print(param = {'error_msg':'Ты слишком молодой, тебе нельзя играть!'})
        break_game()
    elif gamer['age']['answer'] >= 90:
        temp_question = ('Игра может быть слишком утомительна для Вас, вы уверены, что хотите играть?(да/нет)',
                             'Вы точно уверены?(да/нет)',
                             )
        for itm in temp_question:
            while True:
                ask = input(itm + ' ' + exit_str + '\n')
                if ask.lower() == 'exit':
                    break_game()
                elif ask.lower() not in ('да','нет'):
                    error_print(param = {'error_msg':'Неверный ввод. Нужно ввести да или нет'})
                    continue
                elif ask.lower() == 'да':
                    break
                else:
                    print('Игра завершена! до свидания ,', gamer['name']['answer'])
                    break_game()
    return True




def game_not_in_alphabet():
    print('Я выведу все буквы, которых нет в твоем имени')
    alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    for char in alphabet:
        if char not in gamer['name']['answer'].lower():
            print(char)

def game_where_number():
    numbers = [5, 1, 16, 4, 3, 2, 6, 7, 8, 10, 9, 12, 11, 15, 13, 14]
    numbers_copy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    user_numbers = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']

    counter = 0
    for itm in numbers_copy:
        while True:
            print(f"|{user_numbers[0]}|{user_numbers[1]}|{user_numbers[2]}"
                  f"|{user_numbers[3]}|{user_numbers[4]}|{user_numbers[5]}"
                  f"|{user_numbers[6]}|{user_numbers[7]}|{user_numbers[8]}"
                  f"|{user_numbers[9]}|{user_numbers[10]}|{user_numbers[11]}"
                  f"|{user_numbers[12]}|{user_numbers[13]}|{user_numbers[14]}"
                  f"|{user_numbers[15]}|")
            user_answer = input(f'Угадай в какой ячейке находится {itm}. ' + exit_str + '\n')
            counter += 1
            if user_answer.lower() == 'exit':
                break_game()
                break
            if user_answer.isdigit() and 0 < int(user_answer) <= 16:
                if numbers.index(itm) + 1 == int(user_answer):
                    print('Ура, Вы угадали!')
                    user_numbers[numbers.index(itm)] = str(itm)
                    if '*' not in user_numbers:
                        print(f'Поздравляю, вы выйграли!Всего ходов: {counter} ')
                else:
                    print('Попробуйте еще раз...')
                    continue
            else:
                print('Вам нужно ввести число от 1 до 16')
                continue
            break

if __name__ == '__main__':
    print('Допро пожаловать в игру SUPERGAME')
    register_user(**gamer)
    start_game = check_age()

    while start_game:
        start = menu()
        start()

