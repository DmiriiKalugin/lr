import math

print("Операции: Сложение - \"+\", Вычитание - \"-\", Деление - \" / \", Умножение - \" * \", "
      "Возведение в степень - \" ^ \", Sin - \" sin \", Cos - \" cos \", Tg - \" tg \" ")

operation = str(input("Введите операцию - "))
addition = str("+")
subtraction = str("-")
division = str("/")
multiplication = str("*")
degree = str("^")
sin = str("sin")
cos = str("cos")
tg = str("tg")

if operation == addition:
    argument_one = int(input("Введите первое число - "))
    argument_two = int(input("Введите второе число - "))
    result = argument_one + argument_two
    print(result)
elif operation == subtraction:
    argument_one = int(input("Введите первое число - "))
    argument_two = int(input("Введите второе число - "))
    result = argument_one - argument_two
    print(result)
elif operation == division:
    argument_one = int(input("Введите первое число - "))
    argument_two = int(input("Введите второе число - "))
    if argument_two != 0:
        result = argument_one / argument_two
        print(result)
    else:
        print("Деление на 0 невозможно")
elif operation == multiplication:
    argument_one = int(input("Введите первое число - "))
    argument_two = int(input("Введите второе число - "))
    result = argument_one * argument_two
    print(result)
elif operation == degree:
    a = int(input('Введите число - '))
    s = int(input('Вкакую степень возвести - '))
    d = a ** s
    print(a, '^', s, '=', d)
elif operation == sin:
    a = int(input('Введите число - '))
    d = math.sin(a)
    print('sin', a, '=', d)
elif operation == cos:
    a = int(input('Введите число - '))
    d = math.cos(a)
    print('cos', a, '=', d)
elif operation == tg:
    a = int(input('Введите число - '))
    d = math.tan(a)
    print('tan', a, '=', d)
