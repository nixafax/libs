countlow = 0
countup = 0
countnum = 0
countsc = 0
sc="!_*-+()/#%&"
flaws="В пароле нехватает:\n"

pas = input("Введите пароль: ")
if len(pas)<8:
    print("Пароль слишком короткий")
else:
    for i in pas:
        if (i.isupper()) == True:
            countup += 1
        elif (i.islower()) == True:
            countlow += 1
        elif (i.isdigit()) == True:
            countnum += 1
        elif (char in sc for char in i):
            countsc += 1
    if countsc >= 1 and countup >= 1 and countlow >= 1 and countnum >= 1:
        pasr = input("Повторите пароль: ")
        if pas == pasr:
            print("Пароль совпадает")
        else:
            print("Пароль не совпадает")
    else:
        if countlow == 0:
            flaws += "Строчных букв\n"
        if countup == 0:
            flaws += "Заглавных букв\n"
        if countnum == 0:
            flaws += "Цифр\n"
        if countsc == 0:
            flaws += "Специальных символов (" + sc + ")\n"
        print(flaws)