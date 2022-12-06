# Напишите программу, удаляющую из файла все слова, содержащие "абв".

with open('file1.txt', 'r', encoding = 'utf-8') as data:
    txt = data.read()

lst = list(txt.split())

arr = filter(lambda x: 'абв' not in x.lower(), lst)

with open('file1_del.txt', 'w', encoding = 'utf-8') as data1:
    data1.write(' '.join(arr))