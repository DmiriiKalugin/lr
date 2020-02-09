import math

n = int(input("Введите значение n: "))
x = int(input("Введите значение x: "))
if n < 1:
    print("Введите число больше 1")
else:
    print("for: ")
    i = 0
    s = x
    for i in range(n):
        i+=1
        s = math.sin(s) + math.sin(pow(x, i))
        print(s)

print("while: ")
i = 1
s = x
while i < n+1:
    s = math.sin(s) + math.sin(pow(x, i))
    i+=1
    print(s)



