import math

x = int(input("Введите значение X: "))
y = int(input("Введите значение Y: "))
x1 = 4
y1 = 0
x2 = -4
y2 = 0
x3 = 0
y3 = -6
s = (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)
a = (x - x3) * (y2 - y3) - (x2 - x3) * (y - y3)
b = (x1 - x3) * (y - y3) - (x - x3) * (y1 - y3)
c = (x - x2) * (y1 - y2) - (x1 - x2) * (y - y2)

if (s < 0) and (s <= a) and (a <= 0) and (s <= b) and (b <= 0) and (s <= c) and (c <= 0):
    print("Принадлежит")
elif (s > 0) and (s >= a) and (a >= 0) and (s >= b) and (b >= 0) and (s >= c) and (c >= 0):
    print("Принадлежит")
else:
    print("Не принадлежит")



