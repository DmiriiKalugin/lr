import math

a = float(input("Введите значение A - "))
alpha = float(input("Введите значение alpha - "))
b = float(input("Введите значение B - "))
y = math.sin(alpha) + math.cos(2 * b - a)/ math.cos(a) - math.sin(2 * b - a)
z = 1 + math.sin(2 * b) / math.cos(2 * b)

print("y = " + str(y))
print("z = " + str(z))