# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

quarter = int(input('Введите номер четверти (от 1 до 4): '))

if quarter == 1:
    print ('Диапазон координат x: (0; +oo), диапазон координат y: (0; +oo)')
elif quarter == 2:
    print ('Диапазон координат x: (-oo; 0), диапазон координат y: (0; +oo)')
elif quarter == 3:
    print ('Диапазон координат x: (-oo; 0), диапазон координат y: (-oo; 0)')
elif quarter == 4:
    print ('Диапазон координат x: (0; +oo), диапазон координат y: (-oo; 0)')
else:
    print ('Вы ввели некорректное значение')