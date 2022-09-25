# Написать функцию, в которую передается число N. В ней необходимо
# ввести N чисел. Вернуть надо минимум и максимум
# последовательности.
a = False
try:
    serNum = int(input("Введите количество цифр для поиска: "))
    if serNum > 0:
        a = True
    else:
        print("Колличество чисел должно быть больше 0")

except Exception:
    print("Вы ввели не число или не целое число")


def serMaxMin(num):
    try:
        array = []
        i = 0
        while i < num:
            array.append(int(input("Введите число: ")))
            i += 1
        maxNum = array[0]
        minNum = array[0]
        i = 0
        while i < num:
            if array[i] > maxNum:
                maxNum = array[i]
            elif array[i] < minNum:
                minNum = array[i]
            i += 1
        return maxNum, minNum
    except Exception:
        print("колличество цифр для поиска не может быть равна 0 или быть отрицательным а так же не могут быть не числа")


if a == True:
    try:
        ar = serMaxMin(serNum)
        print(
            f"Максимальное число из введеных {ar[0]} и минимальное число {ar[1]}")
    except Exception:
        print("Попробуйте еще раз")
