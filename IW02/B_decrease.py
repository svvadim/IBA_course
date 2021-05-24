# класс объектов, которые одновременно являюстся и
# итерируемыми (есть метод __iter__),
# и итераторами (есть метод __next__);
# преимущества:
# 1. один класс вместо двух - меньше писать и выдумывать названий
# 2. одно общее состояние - не надо передавать переменные

import time


class RangeIterableIterator:
    def __init__(self, size):
        self.x = size

    # раз сам себе итератор - сам себя и возвращает
    def __iter__(self):
        return self

    def __next__(self):
        self.x -= 1
        if self.x <= 0:
            raise StopIteration
        return '#' * self.x


if __name__ == '__main__':
    # создание итерируемого объекта
    main_iter = RangeIterableIterator(32)
    # проход по итерируемому объекту с помощью цикла
    for line in main_iter:
        # вывод текущего элемента (который возвращает итератор)
        print(line)
        # задержка между выводами
        time.sleep(0.25)
