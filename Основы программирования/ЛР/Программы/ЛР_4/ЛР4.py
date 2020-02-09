
a = input('Введите A - ')
b = input('Введите B - ')

if set(b).difference(a):
    print('Нельзя')
else:
    print('Можно')