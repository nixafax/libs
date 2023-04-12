n = 0
sp = {"Россия": "Москва", "Китай": "Пекин", "США": "Вашингтон", "Великобритания": "Лондон", "Франция": "Париж"}
print(sp)

while n != 1:
    capital = input("Введите страну: ")
    if capital in sp.keys():
        print("Столица этой страны: ", sp[capital])
        n = 1
    else:
        print("Такой страны нет в базе данных")

sp = sorted(sp.items(), key=lambda x: x[0])
print(sp)