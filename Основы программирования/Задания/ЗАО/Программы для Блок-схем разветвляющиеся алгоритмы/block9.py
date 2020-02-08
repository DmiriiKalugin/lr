import math

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

k = 0

if b + c > a:
    if a + c > b:
        if a + b < c:
            k = 0
        else:
            k = 2
            if a == c:
                if c == b:
                    k = 3
                    print()
            elif b != c:
                if a != b:
                    k = 1
print(k)
