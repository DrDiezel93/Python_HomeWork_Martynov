# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

import re

with open('file1.txt', 'r') as data1:
    file_1 = data1.readlines()

with open('file2.txt', 'r') as data2:
    file_2 = data2.readlines()

str_file_1 = file_1[0]
str_file_2 = file_2[0]

lst_1 = re.split('[*+=]', str_file_1)
lst_2 = re.split('[*+=]', str_file_2)

for i in range(len(lst_1)):
    if lst_1[i].isdigit():
        lst_1[i] = int(lst_1[i])

for i in range(len(lst_2)):
    if lst_2[i].isdigit():
        lst_2[i] = int(lst_2[i])

print(lst_1)
print(lst_2)

res_pol = []

for i in range(len(lst_1)):
    if type(lst_1[i]) == str:
        if lst_2.count(lst_1[i]) == 0:
            res_pol.append(lst_1[i - 1])
            res_pol.append(lst_1[i])
        elif lst_2.count(lst_1[i]) == 1:
            index = lst_2.index(lst_1[i])
            res_pol.append(lst_1[i - 1] + lst_2[index - 1])
            res_pol.append(lst_1[i])

for j in range(len(lst_2)):
    if type(lst_2[j]) == str:
        if lst_1.count(lst_2[j]) == 0:
            res_pol.append(lst_2[j - 1])
            res_pol.append(lst_2[j])


res_pol.append(lst_1[len(lst_1) - 2] + lst_2[len(lst_2) - 2])
res_pol.append(lst_1[len(lst_1) - 1])

print(res_pol)

for ind in range(1, len(res_pol) - 2, 2):
    with open('res_pol.txt', 'a') as data:
        data.writelines(f'{res_pol[ind - 1]}*{res_pol[ind]}+')

with open('res_pol.txt', 'a') as data:
    data.writelines(f'{res_pol[len(res_pol) - 2]}={res_pol[len(res_pol) - 1]}')