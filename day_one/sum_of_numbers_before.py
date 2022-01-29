import math


def sum_before(number):
    return math.ceil(math.fsum(list(range(number + 1))))


print(sum_before(5))
