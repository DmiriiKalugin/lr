import math

a = int(input("Введите 4-х значное число - "))

m = a
a = m % 10
m = m // 10
b = m % 10
m = m // 10
c = m % 10
d = m // 10

if a == b:
    print("false")
elif a == c:
    print("false")
elif a == d:
    print("false")
elif b == c:
    print("false")
elif b == d:
    print("false")
elif c == d:
    print("false")
else:
    print("true")


