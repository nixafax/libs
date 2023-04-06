from PIL import Image, ImageFilter

for i in range(1, 6):
    name = str(i) + ".png"
    with Image.open(name) as img:
        img_f = img.filter(ImageFilter.EMBOSS)
        new_name = "f_" + name
        img_f.save(new_name)