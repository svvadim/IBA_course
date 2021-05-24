#!/usr/bin/env python3
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D1%82%D1%80%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

# Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и выведите эти числа.

class TribonacciIterator:
    def __init__(self, size):
        self.size = size
        self.first = 0
        self.second = -1
        self.third = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.size -= 1
        if self.size < 0:
            raise StopIteration
        result = self.first + self.second + self.third
        self.first = self.second
        self.second = self.third
        self.third = result
        return f'{result}'


class TribonacciIterableWithGenerator:
    def __init__(self):
        self.first = 0
        self.second = -1
        self.third = 1
        self.i = 0

    def __iter__(self):
        while self.i < 35:
            result = self.first + self.second + self.third
            self.first = self.second
            self.second = self.third
            self.third = result
            self.i += 1
            yield f'{result}'


tribonacciI = TribonacciIterator(35)
for number in tribonacciI:
    print(number)

tribonacciiGen = TribonacciIterableWithGenerator()
for number in tribonacciiGen:
    print(number)
