print('Вас приветствует SuperGame')

gamer = {'name': {'question': 'Как тебя зовут?', 'answer': None},
         'age': {'question': 'Сколько тебе лет?', 'answer': None},
         'sex': {'question': 'Введите ваш пол (м/ж)', 'answer': None},
         'pet_name': {'question': 'Как зовут вашего питомца?', 'answer': None},
         'love_game': {'question': 'Любите ли вы играть (да/нет)', 'answer': None},
         }
exit_str = 'Для выхода введите exit'
temp_answer = True
temp = ''
for itm in gamer:
    if temp_answer:
        while True:
            temp = input(gamer[itm]['question'] + ' ' + exit_str + '\n')
            if temp == 'exit':
                temp_answer = False
                break
            if itm == 'age':
                if temp.isdigit():
                    temp = int(temp)
                else:
                    print('Возраст должен быть числом')
                    continue

            elif itm == 'sex':
                if not (temp == 'м' or temp == 'ж'):
                    print('Пол нужно вводить или м или ж')
                    continue

            elif itm == 'love_game':
                if temp.lower() == 'нет':
                    temp = False
                elif temp.lower() == 'да':
                    temp = True
                else:
                    print('Вы должны ответить да или нет')
                    continue

            gamer[itm]['answer'] = temp
            break
    else:
        break

if temp_answer == True and gamer['age']['answer'] >= 18:
    if gamer['age']['answer'] >= 90:
        temp_question = ('Игра может быть слишком утомительна для Вас, вы уверены, что хотите играть?(да/нет)',
                         'Вы точно уверены?(да/нет)',
                         )
        for itm in temp_question:
            while temp_answer:
                temp_answer = input(itm + ' ' + exit_str + '\n')
                if temp_answer.lower() == 'exit':
                    temp_answer = False
                else:
                    if temp_answer.lower() == 'да':
                        temp_answer = True
                    elif temp_answer.lower() == 'нет':
                        temp_answer = False
                    else:
                        print('Вы должны ответить да или нет')
                        continue
                    break
                if temp_answer:
                    print('Хорошо, тогда начнем игру')

    else:
        print('Привет', gamer['name']['answer'])

if temp_answer:
    print('Я выведу все буквы, которых нет в твоем имени')
    alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    for char in alphabet:
        if char not in gamer['name']['answer'].lower():
            print(char)

numbers = [5, 1, 16, 4, 3, 2, 6, 7, 8, 10, 9, 12, 11, 15, 13, 14]
numbers_copy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
user_numbers = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']

counter = 0
for itm in numbers_copy:
    if temp_answer:
        while temp_answer:
            print(f"|{user_numbers[0]}|{user_numbers[1]}|{user_numbers[2]}"
                      f"|{user_numbers[3]}|{user_numbers[4]}|{user_numbers[5]}"
                      f"|{user_numbers[6]}|{user_numbers[7]}|{user_numbers[8]}"
                      f"|{user_numbers[9]}|{user_numbers[10]}|{user_numbers[11]}"
                      f"|{user_numbers[12]}|{user_numbers[13]}|{user_numbers[14]}"
                      f"|{user_numbers[15]}|")
            user_answer = input(f'Угадай в какой ячейке находится {itm}. ' + exit_str + '\n')
            counter += 1
            if user_answer.lower() == 'exit':
                temp_answer = False
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
    else:
        print(f'Всего ходов: {counter}')
        break

print('Игра завершена! до свидания ,', gamer['name']['answer'])
