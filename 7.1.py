from PIL import Image

with Image.open("ppa.jpg") as i:
    i.show()
    print(i.size)
    print(i.format)
    print(i.mode)