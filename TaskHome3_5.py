# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def NegaFib(num):
    if num in [1, 2]:
        return 1
    else:
        return NegaFib(num + 2) - NegaFib(num + 1)

def Fib(num):
    if num in [1, 2]:
        return 1
    else:
        return Fib(num - 1) + Fib(num - 2)

numb = int(input('Введите целое число: '))
if numb < 0: numb = abs(numb)

lst = []
for item in range(-numb, numb + 1):
    if item <= 0:  
        lst.append(NegaFib(item))
    else:
        lst.append(Fib(item))

print(f'Для k = {numb} cписок будет выглядеть так: {lst}')
