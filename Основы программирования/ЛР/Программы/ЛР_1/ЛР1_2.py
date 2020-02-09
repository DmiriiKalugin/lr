import math

x1 = int(input("Введите значение Х1 - "))
y1 = int(input("Введите значение Y1 - "))
x2 = int(input("Введите значение X2 - "))
y2 = int(input("Введите значение Y2 - "))


ab = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
print("Расстояние между точками равно:  " + str(int(ab)))