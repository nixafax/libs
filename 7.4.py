from PIL import Image, ImageFilter

w_m = Image.open("watermark.png")
for i in range(1, 6):
    name = str(i) + ".png"
    with Image.open(name) as img:
        position = (img.width - w_m.width, img.height - w_m.height)
        img.paste(w_m, position, w_m)
        new_name = "w_" + name
        img.save(new_name)