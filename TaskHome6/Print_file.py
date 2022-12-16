import os
os.chdir(os.path.dirname(__file__))\

import csv


def Print_file():
    with open("Phonebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'{";".join(row)}')
            else:
                print(f'{row[0]} - {row[1]}.')
                count += 1