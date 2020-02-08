import math

x = int(input("Введите X: "))
y = int(input("Введите Y: "))
if x < y:
    Max = y
    Min = x
else:
    Max = x
    Min = y
if x < 0:
    z = Min
else:
    z = Max
print(z)




