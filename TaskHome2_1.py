# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0.56 -> 11

print('Введите вещественное число')

numb = input()

sum = 0

for i in range(len(numb)):
    if numb[i].isdigit():
        sum = sum + int(numb[i])

print(f'{numb} -> {sum}')