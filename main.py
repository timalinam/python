print('Вас приветствует SuperGame')

gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': input('Введите ваш пол\n'),
         'pet_name': input('Как зовут вашего питомца?\n'),
         'love_play': input('Любите ли вы играть? (да/нет)\n'),
         }

if gamer['love_play'] == 'да':
    gamer['love_play'] = True
else:
    gamer['love_play'] = False

if gamer['age'] < 18:
    print('Тебе нельзя играть, потому что тебе меньше 18ти лет.')
elif gamer['age'] > 90:
    answer = input('Для вас это может быть утомительно, вы уверены, что хотите играть?(да\нет)\n')
    if answer == 'нет':
        print('До свидания,', gamer['name'])
    else:
        answer = input('Вы точно уверены, что хотите играть?(да\нет)\n')
        if answer == 'нет':
            print('До свидания,', gamer['name'])
        else:
            print('Хорошо, давайте начнем игру!')

if 90 >= gamer['age'] >= 18:
    print('Я выведу все буквы, которых нет в твоем имени')
    alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    for char in alphabet:
        if char not in gamer['name'].lower():
            print(char)

print('Игра завершена!')
