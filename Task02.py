# Вводятся натуральные числа A и B. (A<B). Функция печатает через
# пробел все простые на отрезке [A,B].

def allOrdinaryNumbers():
    try:
        a = int(input("Введите число А: "))
        b = int(input("Введите число 'B' должно быть больше числа 'А' : "))
        if a >= b:
            print("Вы должны ввести числа. чтобы число А < B")
            allOrdinaryNumbers()
        elif a <= 0 or b <= 0:
            print("Вы должны ввести числа. больше 0")
            allOrdinaryNumbers()
        else:
            array = []
            while a < b+1:
                if a == 1:
                    a += 1
                elif a == 2:
                    array.append(a)
                elif a == 3:
                    array.append(a)
                elif a == 5:
                    array.append(a)
                elif a % 2 != 0 and a % 3 != 0 and a % 5 != 0:
                    array.append(a)
                    a += 1
                a += 1
            return array

    except ValueError:
        print("Вы ввели не числа")


array = allOrdinaryNumbers()
if array != None:
    print(array)
