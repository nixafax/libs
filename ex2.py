otv=""
pl = int(input("Введите номер места: "))
if pl in range (1, 55):
    if pl in range(1, 37):
        otv += "Место в купе "
        if pl%2==0:
            otv += "снизу"
        else:
            otv += "сверху"
    else:
        otv += "Боковое место "
        if pl%2==0:
            otv += "снизу"
        else:
            otv += "сверху"
    print(otv)
else:
    print("Неверно указан номер места")
