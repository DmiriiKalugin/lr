import math
import random

a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
if a == 0:
    if b == 0:
        x = random.randint(1, 100)
        print(x)
    else:
        print("Решений нет")
else:
    x = b / a
    print(x)





