import math

r1 = int(input("Введите радиус большого круга R1: "))
r2 = int(input("Введите радиус меньшего круга R2: "))
s1 = math.pi * pow(r1, 2)
s2 = math.pi * pow(r2, 2)
s = s1 - s2
print(s)





