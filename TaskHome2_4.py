# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

num = int(input('Введите целое число N: '))

num = abs(num)

lst = []

for i in range(-num, num + 1):
    lst.append(i)

print(lst)

index_1 = int(input(f'Введите позицую 1-го элемента от 1 до {len(lst)}: '))
index_2 = int(input(f'Введите позицую 2-го элемента от 1 до {len(lst)}: '))

work = lst[index_1 - 1] * lst[index_2 - 1]

for item in range(1, len(lst)-1):
    str = input('Вы хотите ввести позицию следующего элмента (yes / no): ')
    if str == 'yes' :
        index_item = int(input(f'Введите позицую следующего элемента от 1 до {len(lst)}: '))
        work = work * lst[index_item - 1]
    else:
        break

print(work)