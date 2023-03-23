f = open("Export.txt")
f1 = open("Export(remake).txt", "w")
data = ""

for i in range(57):
    data = data + f.readline()

for line in f.readlines():
    i = line.split("\t")
    if "in  Word" in i[7]:
        pr = i[7].split()
        if 8 <= int(pr[0]) <= 15:
            pr[0] = int(pr[0])-8
            pr_db = int(pr[3][2:5]) * 2
            pr_dw = pr[3].split(",")
            rep = "DB" + str(pr_db) + "," + pr_dw[1] + "." + str(pr[0])
        else:
            pr_db = int(pr[3][2:5]) * 2 + 1
            pr_dw = pr[3].split(",")
            rep = "DB" + str(pr_db) + "," + pr_dw[1] + "." + pr[0]
        line = line.replace(i[7], rep)
        data = data + line
        # print("inw")
    else:
        pr = i[7].split(",")
        pr_d = int(pr[1][2:]) * 2
        if pr[1][1] == "W":
            rep = pr[0] + "," + "DBW" + str(pr_d)
        else:
            rep = pr[0] + "," + "DBD" + str(pr_d)
        line = line.replace(i[7], rep)
        data = data + line
        # print("123")

f1.write(data)

f.close()
f1.close()