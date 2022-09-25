# Task01

# В математике функция sign(x) (знак числа) определена так:
# sign(x) = 1, если x > 0,
# sign(x) = -1, если x < 0,
# sign(x) = 0, если x = 0
# Напишите эту функцию

def sign():
    try:
        x = int(input("Введите число: "))
        if x > 0:
            return 1
        elif x < 0:
            return -1
        elif x == 0:
            return 0
    except ValueError:
        print("Вы ввели не число")


rez = sign()
if rez != None:
    print(rez)
