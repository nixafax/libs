from PIL import Image, ImageOps

with Image.open("ppa.jpg") as i:
    imv = ImageOps.mirror(i)
    imv.save("ppa_v.png")
    img = ImageOps.flip(i)
    img.save("ppa_g.png")
    (width, height) = (img.width // 3, img.height // 3)
    i_r = i.resize((width, height))
    i_r.save("ppa_r.png")