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
    answer = input('Для вас это может быть утомительно, вы уверены, что хотите играть?(да\нет)')
    if answer = 'нет':
        print('До свидания,', gamer['name'])
    else:
        answer = input('Вы точно уверены, что хотите играть?(да\нет)')
        if answer = 'нет':
            print('До свидания,', gamer['name'])
        else:
            print('Хорошо, давайте начнем игру!')


if 90 >= gamer['age'] > 18:

    print('Я могу сосчитать твой возраст')

i = 0
while i <= gamer['age']:
    print(i)
    i += 1

    if i > 22:
        print('замучился считать')
        break
else:
    print('Сработал else в цикле')

print('А еще я могу произнести имя по буквам')

i = 0
for char in gamer['name']:
    i += 1
    if i == 3:
        continue
    print(char)