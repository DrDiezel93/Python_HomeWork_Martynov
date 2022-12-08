# Создайте программу для игры в "Крестики-нолики".
# Вариант интерфейса:
#  1  |  2 | 3
# --------------
#  4  |  5 | 6
# --------------
#  7  |  8 | 9

def print_game(ls1, ls2, ls3):
    print()
    print(f' {ls1[0]} | {ls1[1]} | {ls1[2]}')
    print(' ---------')
    print(f' {ls2[0]} | {ls2[1]} | {ls2[2]}')
    print(' ---------')
    print(f' {ls3[0]} | {ls3[1]} | {ls3[2]}')
    print()


lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]

print_game(lst1, lst2, lst3)

for i in range(1, 6):
    x1 = int(input('Введите позицию для крестика: '))
    if 1 <= x1 <= 3: 
        lst1[lst1.index(x1)] = 'X'
    elif 4 <= x1 <= 6: 
        lst2[lst2.index(x1)] = 'X'
    elif 7 <= x1 <= 9: 
        lst3[lst3.index(x1)] = 'X'
    else: 
        print('Вы ввели некорректное значение')
        break
    if all([j == 'X' for j in lst1]) or all([k == 'X' for k in lst2]) or all([m == 'X' for m in lst3]):
        print()
        print_game(lst1, lst2, lst3)
        print('Крестики победили')
        print()
        break
    elif (lst1[0] == 'X' and lst2[0] == 'X' and lst3[0] == 'X' or lst1[1] == 'X' and lst2[1] == 'X' and lst3[1] == 'X' or 
    lst1[2] == 'X' and lst2[2] == 'X' and lst3[2] == 'X' or lst1[0] == 'X' and lst2[1] == 'X' and lst3[2] == 'X'or 
    lst1[2] == 'X' and lst2[1] == 'X' and lst3[0] == 'X'):
        print()
        print_game(lst1, lst2, lst3)
        print('Крестики победили')
        print()
        break
    print_game(lst1, lst2, lst3)
    if i == 5: 
        print('Вы сыграли в ничью')
        print()
        break
    o1 = int(input('Введите позицию для нолика: '))
    if 1 <= o1 <= 3: 
        lst1[lst1.index(o1)] = 'O'
    elif 4 <= o1 <= 6: 
        lst2[lst2.index(o1)] = 'O'
    elif 7 <= o1 <= 9: 
        lst3[lst3.index(o1)] = 'O'
    else: 
        print('Вы ввели некорректное значение')
        break
    if all([j == 'O' for j in lst1]) or all([k == 'O' for k in lst2]) or all([m == 'O' for m in lst3]):
        print()
        print_game(lst1, lst2, lst3)
        print('Крестики победили')
        print()
        break
    elif (lst1[0] == 'O' and lst2[0] == 'O' and lst3[0] == 'O' or lst1[1] == 'O' and lst2[1] == 'O' and lst3[1] == 'O' or 
    lst1[2] == 'O' and lst2[2] == 'O' and lst3[2] == 'O' or lst1[0] == 'O' and lst2[1] == 'O' and lst3[2] == 'O'or 
    lst1[2] == 'O' and lst2[1] == 'O' and lst3[0] == 'O'):
        print()
        print_game(lst1, lst2, lst3)
        print('Нолики победили')
        print()
        break
    print_game(lst1, lst2, lst3)