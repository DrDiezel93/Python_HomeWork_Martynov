# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_1 = [1.1, 1.2, 3.1, 5, 10.01]


def DiffFloatNumbMaxMin(lst):
    max_float = lst[0] % 1
    min_float = lst[0] % 1
    for i in range(1, len(lst)):
        if lst[i] % 1 > max_float and lst[i] % 1 != 0:
            max_float =  lst[i] % 1
        elif lst[i] % 1 < min_float and lst[i] % 1 != 0:
            min_float = lst[i] % 1
    
    dif = round((max_float - min_float), 3)
    print(f'{lst} => {dif}')


DiffFloatNumbMaxMin(list_1)