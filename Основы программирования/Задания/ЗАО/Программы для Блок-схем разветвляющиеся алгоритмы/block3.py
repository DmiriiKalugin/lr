import math
import random

H = int(input("Введите значение H: "))
h = int(input("Введите значение h: "))
if H <= 100:
    if h >= 60:
        if (H - h) >= 30:
            print("Нормальное")
        else:
            print("Пониженное")
    else:
        print("Пониженное")
else:
    print("Повышенное")





