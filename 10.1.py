import json

f = open("123.json", mode="r", encoding="UTF8")
j_d = json.load(f)
for i in range (0, len(j_d["products"])):
    data = j_d["products"][i]
    print("Название:", data["name"], "\n", "Цена:", data["price"], "\n", "Вес:", data["weight"])
    if data["available"] == True:
        print(" В наличии")
    else:
        print(" Нет в наличии!")
f.close()