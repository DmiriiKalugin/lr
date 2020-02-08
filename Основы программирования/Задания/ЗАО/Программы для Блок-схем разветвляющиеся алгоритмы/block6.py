x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
R = float(input("Введите значение R: "))
r = float(input("Введите значение r: "))
if (pow(x, 2) + pow(y, 2)) > pow(R, 2):
    print(pow(x, 2) + pow(y, 2))
    if (pow(x, 2) + pow(y, 2)) < pow(r, 2):
        print("Принадлежит")
    else:
        print("Не принадлежит")
else:
    print("Не принадлежит")