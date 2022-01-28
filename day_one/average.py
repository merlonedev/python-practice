import math

def average(numbers):
    sum = math.fsum(numbers)
    return sum / len(numbers)

print(average([2, 4, 5, 10, 15]))
