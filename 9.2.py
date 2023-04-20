import os
import shutil
from PIL import Image, ImageFilter

n = 0

while n == 0:
    col = 0
    path = input("Введите путь к файлам: ")
    type = input("Введите тип файлов: ")
    for i in range(1, 6):
        name = str(i) + "." + type
        path_file = path + "/" + name
        if os.path.isfile(path_file):
            col += 1
    if col == 5:
        n += 1
    if n == 0:
        print("Файлы не найдены")

os.mkdir("f_12345")
for i in range(1, 6):
    name = str(i) + "." + type
    with Image.open(name) as img:
        img_f = img.filter(ImageFilter.EMBOSS)
        new_name = "f_" + name
        img_f.save(new_name)
        path_source = path + "/" + new_name
        path_destination = path + "/" + "f_12345"
        shutil.move(path_source, path_destination)