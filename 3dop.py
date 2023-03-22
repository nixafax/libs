f = open("news.txt")
positive = 0

for line in f.readlines():
    line = line.replace("\n", "")
    i = line.split(" ",1)
    if positive < int(i[0]):
        print(i[1])
        positive = int(i[0])

f.close()