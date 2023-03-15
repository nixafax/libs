import sys
import re
pr = ""
mass = []
word = (input("Введите слово к которому надо подобрать синоним: ")).lower()
words = word.lower() + " "
wordn = word.lower() + "\n"
wordt = word.lower() + ";"
f = open("synonyms.txt")
for line in f.readlines():
    line = line.lower()
    if line.find(words) != -1 or line.find(wordn) != -1 or line.find(wordt) != -1:
        i = re.split(';|-', line)
        mass.extend(i)

for i in range(0, len(mass)):
    if mass[i].find("\n") != -1:
        mass[i] = mass[i].replace("\n","")
    if mass[i][0] == " ":
        mass[i] = mass[i][1:len(mass[i])]
    if mass[i][-1] == " ":
        mass[i] = mass[i][0:len(mass[i])-1]

if mass == []:
    print("Такого слова нет в базе данных")
    sys.exit()
for st in mass:
    if word != st:
        print("Синоним к данному слову: ", st)
        pr = input("подходит ли данное слово? (yes/no): ")
        if pr == "yes":
            sys.exit()
add = input("Внесите свой вариант: ")
add = add.lower()
f.seek(0)
for line in f.readlines():
    fixline = line
    line = line.lower()
    if line.find(words) != -1 or line.find(wordn) != -1 or line.find(wordt) != -1:
        newstr = fixline.replace("\n", "; " + add + "\n")
        oldstr = fixline
f.seek(0)
old_data = f.read()
f.close()

f = open("synonyms.txt", "w")
new_data = old_data.replace(oldstr, newstr)
f.write(new_data)
f.close()