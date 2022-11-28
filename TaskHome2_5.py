# 5 Реализуйте алгоритм перемешивания списка.

# Алгоритм перетасовки Фишера–Йейтса

from random import randint

def randomize(arr):
    for i in range(len(arr)):
        j = randint(0, len(arr) - 1)
        arr[i], arr[j] = arr[j], arr[i]

array = [1, 2, 3, 4, 5, 6, 7, 8]
randomize(array)
print(array)