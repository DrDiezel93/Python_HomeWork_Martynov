# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

lst_1 = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]

# lst_2 = []
# for item in lst_1:
#     if lst_1.count(item) == 1:
#         lst_2.append(item)

lst_2 = list(filter(lambda x: lst_1.count(x) == 1, lst_1))

print(f'при {lst_1} - > {lst_2}')