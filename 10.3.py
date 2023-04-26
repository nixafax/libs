import sys
import re

def fix_mass(mass):
    for i in range(0, len(mass)):
        if mass[i].find("\n") != -1:
            mass[i] = mass[i].replace("\n", "")
        if mass[i][0] == " ":
            mass[i] = mass[i][1:len(mass[i])]
        if mass[i][-1] == " ":
            mass[i] = mass[i][0:len(mass[i]) - 1]
    return mass

data = []
f = open("en-ru.txt", mode="r", encoding="UTF8")
for line in f.readlines():
    mass = re.split(',|-', line)
    mass = fix_mass(mass)
    for i in range (1, len(mass)):
        mass_in_data = []
        mass_in_data.append(mass[i])
        mass_in_data.append(mass[0])
        data.append(mass_in_data)

Del = [] #список с элиментами которые надо удолить
for i in range (0, len(data)-1):
    for j in range (i+1, len(data)):
        if data[i][0] == data[j][0]:
            Del.append(j)
            data[i].append(data[j][1])
for i in Del:
    data.pop(i)
data.sort()
f.close()

new_data = ""
for i in data:
    new_data = new_data + i[0] + " - " + i[1]
    for j in range (2, len(i)):
        new_data = new_data + ", " + i[j]
    new_data = new_data + "\n"

f = open("ru-en.txt", "w")
f.write(new_data)
f.close()