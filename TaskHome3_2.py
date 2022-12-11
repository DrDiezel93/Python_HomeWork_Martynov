# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math

lst_1 = [2, 3, 4, 5, 6]
lst_2 = [2, 3, 5, 6]

# def MultiPairsNumb (lst):
#     multi_lst = []
#     for i in range(math.ceil(len(lst) / 2)):
#         multi_lst.append(lst[i] * lst[(-i) - 1])
#     print(f'{lst} => {multi_lst}')

multi_lst_1 = [lst_1[i] * lst_1[(-i) - 1] for i in range(math.ceil(len(lst_1) / 2))]
multi_lst_2 = [lst_2[i] * lst_2[(-i) - 1] for i in range(math.ceil(len(lst_2) / 2))]


print(multi_lst_1)
print(multi_lst_2)