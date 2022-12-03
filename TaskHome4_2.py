# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]

def ListOfPrimeFactors(numb):
    lst = [] 
    i = 2
    while numb > 1:
        if numb % i == 0:
            lst.append(i)
            numb = numb // i
        else: 
            i = i + 1
    return lst

n =  int(input("Введите целое положительное число: "))

if n < 0:
    print('Вы ввели отрицательное число, но мы Вас поправили')
    n = abs(n)
    print(f'при N = {n} список простых множителей выглядит так -> {ListOfPrimeFactors(n)}')
else: print(f'при N = {n} список простых множителей выглядит так -> {ListOfPrimeFactors(n)}')