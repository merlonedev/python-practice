import os

os.chdir("day_two")


def get_recuperation_students():
    in_recuperation = []
    with open("students.txt") as file:
        for line in file:
            name = line.split(" ")[0]
            grade = line.split(" ")[1]
            if not int(grade) > 5:
                in_recuperation.append(f"{name}\n")
    return in_recuperation


def write_recuperation_file():
    in_recuperation = get_recuperation_students()
    with open("recuperation.txt", "w") as file:
        for student in in_recuperation:
            file.writelines(student)


write_recuperation_file()
