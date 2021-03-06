#!/usr/bin/env python3


# Task 2 variant 1

# Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
# Могут ли два билета подряд быть удачными?

def sum_digit(num):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result


# replace 100000 with 1 if the ticket number starts with 1
for i in range(100000, 1000000):
    if sum_digit(i) % 7 == 0 and sum_digit(i + 1) % 7 == 0:
        print(str(i) + ' and ' + str(i + 1))
