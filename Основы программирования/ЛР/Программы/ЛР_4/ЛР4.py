
a = input('Введите первое слово - ')
b = input('Введите второе слово - ')

if set(b).difference(a):
    print('составить нельзя')
else:
    print('составить можно')