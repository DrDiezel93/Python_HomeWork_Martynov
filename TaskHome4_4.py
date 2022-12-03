# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k =  int(input("Введите натуральную степень k =  "))

name = input('Введите имя файла: ')

if k > 1:
    for i in range(k, 1, -1):
        coeff = randint(0, 100)
        if coeff != 0 and coeff != 1:
            with open(f'{name}.txt', 'a') as data:
                data.writelines(f' {coeff}*x^{i} +')
        if coeff == 1:
            with open(f'{name}.txt', 'a') as data:
                data.writelines(f' x^{i} +')

with open(f'{name}.txt', 'a') as data:
    coeff_1 = randint(0, 100)
    if coeff_1 != 0 and coeff_1 != 1:
        data.writelines(f' {coeff_1}*x +')
    elif coeff_1 == 1:
            with open(f'{name}.txt', 'a') as data:
                data.writelines(f' x^{i} +')
    

with open(f'{name}.txt', 'a') as data:
    coeff_2 = randint(0, 100)
    if coeff_2 != 0:
        data.writelines(f' {coeff_2} = 0')
    else: data.writelines(f' 0 = 0')