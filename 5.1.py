import random

mas = []
for i in range (0, 5):
    x = random.randint(0, 100)
    mas.append(x)

number = int(input("Ведите число: "))
if number in mas:
    print("Массив чисел: ", *mas, " Введённое число: ", number, "\n", "Поздравляю, Вы угадали число!")
else:
    print("Массив чисел: ", *mas, " Введённое число: ", number, "\n", "Нет такого числа!")