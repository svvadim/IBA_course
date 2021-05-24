#!/usr/bin/env python3
# Task 2 variant 11
# Скопировать из файла F1.txt в файл F2 все строки, которые содержат только одно слово.
# Найти самое короткое слово в файле F2.

def main(from_file, to_file):
    f_file = open(from_file, "r")
    t_file = open(to_file, "w")
    lines = []
    for line in f_file:
        if line.count(' ') == 0:
            lines.append(line)
    f_file.close()
    t_file.writelines(lines)
    min_line = min((word for word in lines if word), key=len)
    t_file.close()
    return min_line


print(main("F1.txt", "F2.txt"))
