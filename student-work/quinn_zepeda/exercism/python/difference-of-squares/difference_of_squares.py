def square_of_sum(number):
    count = 0
    for i in range(1,number + 1):
        count += i
    c_squared = count**2
    return c_squared

def sum_of_squares(number):
    total = 0
    for i in range(1,number + 1):
        total = total + (i**2)
    return total


def difference(number):
    first = square_of_sum(number)
    second = sum_of_squares(number)
    total = abs(first - second)
    return total
