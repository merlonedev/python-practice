import os
import csv

os.chdir("day_two")

with open("balneabilidade.csv") as file:
    beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = beach_status_reader

print(data)
