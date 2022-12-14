# 3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52] -> 14.072    (Округлять не обязательно)

n = int(input('Введите целое число n: '))

lst = []

for i in range(1, n + 1):
    lst.append((1 + 1 / i) ** i)
    lst[i - 1]= round(lst[i - 1], 2)

print(f'Для n = {n}: {lst} -> {sum(lst)}')