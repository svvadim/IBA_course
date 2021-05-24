#!/usr/bin/env python3
# Task 2 variant 11
# Скопировать из файла F1.txt в файл F2 все строки, которые содержат только одно слово.
# Найти самое короткое слово в файле F2.

def main(from_file, to_file):
    with open(from_file, "r") as f_file:
        lines = [line for line in f_file if line.count(' ') == 0]
    with open(to_file, "w") as t_file:
        t_file.writelines(lines)
    return min((word for word in lines if word), key=len)


print(main("F1.txt", "F2.txt"))
