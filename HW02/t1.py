#!/usr/bin/env python3


a = int(input("Введите сторону a "))
b = int(input("Введите сторону b "))


def break_into_squares(a, b):
    if a == 0 or b == 0:
        return
    if a > b:
        print("Квадрат со стороной ", b, " и ", b)
        break_into_squares(a - b, b)
    else:
        print("Квадрат со стороной ", a, " и ", a)
        break_into_squares(a, b - a)


break_into_squares(a, b)
