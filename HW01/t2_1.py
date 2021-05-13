#!/usr/bin/env python3


# Task 2 variant 1

# Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
# Могут ли два билета подряд быть удачными?

def sum_dijit(num):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result


for i in range(100000, 1000000):
    if sum_dijit(i) % 7 == 0 and sum_dijit(i + 1) % 7 == 0:
        print(str(i) + ' and ' + str(i + 1))
