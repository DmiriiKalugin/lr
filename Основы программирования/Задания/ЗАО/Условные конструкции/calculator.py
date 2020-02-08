import math

argument_one = int(input("Введите первое число - "))
argument_two = int(input("Введите второе число - "))
operation = str(input("Введите операцию - "))
addition = str("+")
subtraction = str("-")
division = str("/")
multiplication = str("*")
result = 0

if operation == addition:
    result = argument_one + argument_two
    print(result)
elif operation == subtraction:
    result = argument_one - argument_two
    print(result)
elif operation == division:
    if argument_two != 0:
        result = argument_one / argument_two
        print(result)
    else:
        print("Деление на 0 невозможно")
elif operation == multiplication:
    result = argument_one * argument_two
    print(result)
