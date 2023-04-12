from PIL import Image, ImageDraw, ImageFont
n = 0
sp = {"новый год": "postcard.jpg", "день рождения": "dr.jpg", "8 марта": "8m.jpg", "23 февраля": "23f.jpg"}

while n != 1:
    holiday = input("Введите праздник: ").lower()
    if holiday in sp.keys():
        img = Image.open(sp[holiday])
        img2 = Image.open(sp[holiday])
        n = 1
    else:
        print("Такого праздника нет в базе данных")

name = input("Ведите имя того, кого надо поздравить: ")
name = name + ", поздравляю!"

font = ImageFont.truetype("arial.ttf", 40)
draw_text = ImageDraw.Draw(img)
W = img.width
H = img.height
w, h = draw_text.textsize(name, font=font)
draw_text.text(((W - w)/2, 0), name, (0, 0, 0), font=font)
img.save("draw_text.png")

font = ImageFont.truetype("arial_bold.ttf", 40)
draw_text2 = ImageDraw.Draw(img2)
W = img2.width
H = img2.height
w, h = draw_text2.textsize(name, font=font)
draw_text2.text(((W - w)/2, (H - h)), name, (255, 0, 0), font=font)
img2.save("draw_text2.png")