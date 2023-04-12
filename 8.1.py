from PIL import Image

with Image.open("dr.jpg") as i:
    i.crop((225, 250, 500, 525)).save("dr_crop.jpg")