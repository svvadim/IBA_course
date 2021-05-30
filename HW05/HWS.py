def break_into_squares(a, b, count=0):
    if a == 0 or b == 0:
        return count
    if a > b:
        return break_into_squares(a - b, b, count + 1)
    else:
        return break_into_squares(a, b - a, count + 1)


def sum_digit(num):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result


def lucky_tickets(start=100000, stop=1000000):
    # replace 100000 with 1 if the ticket number starts with 1
    result = []
    for i in range(start, stop):
        if sum_digit(i) % 7 == 0 and sum_digit(i + 1) % 7 == 0:
            result.append(str(i) + ' and ' + str(i + 1))
    return result
