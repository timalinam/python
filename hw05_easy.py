# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

this_folder = os.getcwd()
name_folders = [f'dir_{i}' for i in range(1, 10)]
name_dirs = [f'{os.path.join(this_folder,name_folder)}' for name_folder in name_folders]
def add_folders(*args):
    for name_dir in args:
        try:
            if not os.path.exists(name_dir):
                os.makedirs(name_dir)
                print('Папка создана')
            else:
                print('Папка уже существует')
        except OSError:
            print('Произошла ошибка, проверьте правильность ввода')
def dell_folders(*args):
    for name_dir in args:
        try:
            if os.path.exists(name_dir):
                os.rmdir(name_dir)
                print('Папка удалена')
            else:
                print('Папка не найдена')
        except OSError:
            print('Произошла ошибка, проверьте правильность ввода')



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def print_folders():
    print(list(filter(lambda x: os.path.isdir(x), os.listdir(os.getcwd()))))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil

def copy_this_file():
    file_name, file_extension = os.path.splitext(__file__)
    if not os.path.exists(f'{file_name}_copy{file_extension}'):
        shutil.copyfile(os.path.join(os.getcwd(), __file__), f'{file_name}_copy{file_extension}')
    else:
        print('Копия текущего файла уже существует')


if __name__ == '__main__':
    add_folders(*name_dirs)
    print_folders()
    dell_folders(*name_dirs)
    print_folders()
    copy_this_file()