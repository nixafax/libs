import json

new_product = {}
new_product["name"] = input("Введите название продукта: ")
new_product["price"] = input("Введите цену продукта: ")
new_product["weight"] = input("Введите вес продукта: ")
available = input("Есть ли он в наличии (да/нет): ")
if available == "да":
    new_product["available"] = True
else:
    new_product["available"] = False

f = open("123.json", mode="r", encoding="UTF8")
j_d = json.load(f)
j_d["products"].append(new_product)
f.close()

f = open("123.json", mode="w", encoding="UTF8")
json.dump(j_d, f)
f.close()

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