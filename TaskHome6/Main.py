import os
os.chdir(os.path.dirname(__file__))

from os.path import exists
from CSV_creating import creating
from File_writing import writing_scv
from Print_file import Print_file
from User_interface import get_info

user = input('Вы хотите просмотреть ваш список контактов?(Да / Нет): ')
if user == 'Да':
    path = 'Phonebook.csv'
    valid = exists(path)
    if not valid:
        print('Ваш список контактов пуст')
        user_1 = input('Вы хотите добавить контакт?(Да / Нет): ')
        if user_1 == 'Да':
            creating()
            writing_scv(get_info())
            print('Контакт добавлен')
        else: print('Всего доброго')
    else:
        Print_file()
elif user == 'Нет':
    user_2 = input('Вы хотите добавить контакт?(Да / Нет): ')
    if user_2 == 'Да':
        path = 'Phonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
            writing_scv(get_info())
            print('Контакт добавлен')
        else: 
            writing_scv(get_info())
            print('Контакт добавлен')
    else: print('Всего доброго')
else: print('Всего доброго')