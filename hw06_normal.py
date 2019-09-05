# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


# 1. school.rooms_dict.keys
# 2. school.room_dict["11A"].list_students()
# 3. ищем ученика по всем класса. запоминаем его класс. выводим предметы.
# 4. student.parents = ["мама фио", "папа фио"]. Ищем ученика по класса. Выводим родитиелей
# 5. rooms.lessons, lessons.teachers. Получаем класс. Получаем предметы. Берем учителей по предметам из словаря.

class School:
    def __init__(self):
        self.rooms = {}
        self.lessons_to_teachers = {}

class Room:
    def __init__(self, name):
        self.name = name
        self.lessons = []
        self.students = {}

    def add_student(self, surname, name, middle_name, mother, father):
        # self.name = f'{self.surname} {self.name[0]}.{self.middle_name[]}'
        self.students[surname] = Student(surname, name, middle_name, mother, father)

class Student:
    def __init__(self, surname, name, middle_name, mother, father):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.parents = []
        self.parents.append(mother)
        self.parents.append(father)

    def __repr__(self):
        return f'{self.surname} {self.name[0]}.{self.middle_name[0]}'


school = School()
school.lessons_to_teachers["Английский язык"] = "Истан Д.С."
school.lessons_to_teachers["Русский язык"] = "Романюк В.Ф."
school.lessons_to_teachers["Математика"] = "Углич Т.В."
school.lessons_to_teachers["Физкультура"] = "Ромашка И.В"
school.lessons_to_teachers["ИЗО"] = "Камач И.Д."
school.lessons_to_teachers["Музыка"] = "Шаро И.С."


room1 = Room("1a")
room1.lessons.append("Математика")
room1.lessons.append("Русский язык")
room1.add_student("Паран", 'Ульяна', 'Игоревна', "Паран М.С.", "Паран И.Г.")
room1.add_student("Ананас", 'Ирина', 'Михайловна', "Ананас Р.М.", "Ананс М.И.")

room2 = Room("2a")
room2.lessons.append("Русский язык")
room2.lessons.append("Математика")
room2.lessons.append("Английский язык")
room2.lessons.append("Физкультура")
room2.add_student("Змея", 'Надежда', 'Леонидовна', "Змея Р.М.", "Змея Л.В.")
room2.add_student("Дуб", 'Алексей', 'Павлович', "Дуб И.Г.", "Дуб П.С.")

room3 = Room("3a")
room3.lessons.append("Русский язык")
room3.lessons.append("Математика")
room3.lessons.append("Английский язык")
room3.lessons.append("Физкультура")
room3.lessons.append("ИЗО")
room3.add_student("Любавина", 'Светлана', 'Геннадьевна', "Любавина Т.С.", "Любавин Г.Т.")
room3.add_student("Воронец", 'Алексей', 'Тимурович', "Воронец Т.Ф.", "Воронец Т.Т.")

room4 = Room("4a")
room4.lessons.append("Русский язык")
room4.lessons.append("Математика")
room4.lessons.append("Английский язык")
room4.lessons.append("Физкультура")
room4.lessons.append("ИЗО")
room4.lessons.append("Музыка")
room4.add_student("Иванова", 'Ирина', 'Михайловна', "Иванова Р.М.", "Иванов М.И.")
room4.add_student("Ким", 'Анжелика', 'Романовна', "Ким П.М.", "Ким Р.Т.")


school.rooms["1a"] = room1
school.rooms["2a"] = room2
school.rooms["3a"] = room3
school.rooms["4a"] = room4


# 1. Получить полный список всех классов школы
print("1: ", *school.rooms.keys())
# 2. Получить список всех учеников в указанном классе
answer = '1a'
print("2: ", *school.rooms[answer].students.values())
# 3. Получить список всех предметов указанного ученика
print("3:")
answer = 'Ананас'
for room in school.rooms.values():
    if answer in room.students:
        print(*room.lessons)

# 4. Узнать ФИО родителей указанного ученика
print("4:")
answer = 'Ананас'
for room in school.rooms.values():
    for student in room.students.values():
        if student.surname == answer:
            print(*student.parents)
# 5. Получить список всех Учителей, преподающих в указанном классе
print("5:")
answer = '4a'
for lesson in school.rooms[answer].lessons:
    print(school.lessons_to_teachers[lesson])
