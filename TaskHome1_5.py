# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print ('Введите координаты точки А')
xA = int(input('A(x): '))
yA = int(input('A(y): '))
print ('Введите координаты точки B')
xB = int(input('B(x): '))
yB = int(input('B(y): '))

dist = round (((xB - xA)**2 + (yB - yA)**2)**0.5, 2)
dist = float(int(dist * 100)/100)
str_dist = str(dist).replace(".", ",")
print (f'A {xA, yA}, B {xB, yB} -> {str_dist}')