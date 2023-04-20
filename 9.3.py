import csv
with open("data.csv", encoding='cp1251') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")       # Создаем объект reader, указываем символ-разделитель ","
    print("Нужно купить:")
    sum = 0
    for row in file_reader:
        print(f"{row[0]} - {row[1]} шт. за {row[2]} руб.")
        sum += int(row[2]) * int(row[1])
    print(f"Итоговая сумма: {sum} руб.")