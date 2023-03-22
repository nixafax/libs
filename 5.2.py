import random

mas = []
rmas = []
for i in range (0, 10):
    x = random.randint(0, 10)
    mas.append(x)

for a in range(0, len(mas)):
    for b in range(0, len(mas)):
        if b != a and mas[b] == mas[a] and not(mas[b] in rmas):
            rmas.append(mas[b])
if len(rmas) == 0:
    print("Массив чисел: ", *mas, "\nПовторяющихся элиментов нет")
else:
    print("Массив чисел: ", *mas, "\nПовторяющиеся элименты: ", *rmas)