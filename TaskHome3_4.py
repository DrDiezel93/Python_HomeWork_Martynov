# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

numb = int(input('Введите положительное целое число: '))


def BinNumb(num):
    if num == 0: return
    BinNumb(int(num / 2))
    print(f'{num % 2}', end='')


print(bin(numb))
BinNumb(numb)