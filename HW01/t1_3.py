#!/usr/bin/env python3


# Task 1 variant 3

# Даны три числа a, b и c. Найти среднее геометрическое этих чисел,
# если все они отличны от нуля, и среднее арифметическое в противном случае.

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if a and b and c:
    print((a * b * c) ** (1 / 3))
else:
    print((a + b + c) / 3)
