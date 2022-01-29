import sys


def sum_values(numbers: str):
    numbers = numbers.split(" ")
    total = 0
    for number in numbers:
        if not number.isdigit():
            print(
                f"Erro ao somar valores, '{number}' é um valor inválido",
                file=sys.stderr,
            )
        else:
            total += int(number)
    return total


numbers = input("Digite números, separados por espaço: ")
print(sum_values(numbers))
