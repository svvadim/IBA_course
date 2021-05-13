#!/usr/bin/env python3
import random

# Task 3 variant 5

# Для каждого четного по номеру элемента списка A найти его сумму со следующим элементом
# и записать эти суммы в новый список B.

list_size = int(input("Enter list length "))
A = [random.randint(0, 99) for i in range(list_size)]
B = []

for i in range(1, list_size, 2):
    B.append(A[i] + A[i - 1])

print(A)
print(B)
