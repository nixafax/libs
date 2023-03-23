n = 0
sp = {"Россия": "Москва", "Китай": "Пекин", "США": "Вашингтон", "Великобритания": "Лондон", "Франция": "Париж"}
print(sp)
capital = input("Введите страну: ")

while n != 1:
    if capital in sp.keys():
        print("Столица этой страны: ", sp[capital])
        n = 1
    else:
        print("Такой страны нет в базе данных")

sp = sorted(sp.items(), key=lambda x: x[0])
print(sp)