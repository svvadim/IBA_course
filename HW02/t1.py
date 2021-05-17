#!/usr/bin/env python3


a = int(input("Введите сторону a "))
b = int(input("Введите сторону b "))


def break_into_squares(a, b, count=0):
    if a == 0 or b == 0:
        print("Всего ", count)
        return
    if a > b:
        print("Квадрат со стороной ", b, " и ", b)
        break_into_squares(a - b, b, count + 1)
    else:
        print("Квадрат со стороной ", a, " и ", a)
        break_into_squares(a, b - a, count + 1)


break_into_squares(a, b)
