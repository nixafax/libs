from PIL import Image
n = 0
sp = {"новый год": "postcard.jpg", "день рождения": "dr.jpg", "8 марта": "8m.jpg", "23 февраля": "23f.jpg"}

while n != 1:
    holiday = input("Введите праздник: ").lower()
    if holiday in sp.keys():
        i = Image.open(sp[holiday])
        i.show()
        n = 1
    else:
        print("Такого праздника нет в базе данных")