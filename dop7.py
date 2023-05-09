from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

price = {1: 15, 2: 20.5, 3: 60}

def is_valid(newval):
    return newval == "" or newval.isnumeric()

def calculation():
    vl = txt1.get()
    if vl == "" or radio.get() == 0:
        txt2["state"] = "normal"
        txt2.delete(0, END)
        txt2.insert(0, "Сначала введите данные")
        txt2["state"] = "readonly"
    else:
        vl2 = price[radio.get()]
        ot = "Итоговая цена: " + str(int(vl)*vl2) + " руб."
        txt2["state"] = "normal"
        txt2.delete(0, END)
        txt2.insert(0, ot)
        txt2["state"] = "readonly"

window = Tk()
window.title("Фотоателье")
window.geometry("600x450")

style = Style(window)
style.configure("TRadiobutton", background = "#C0C0C0", font = ("impact", 25))
style.configure("TLabel", background = "#C0C0C0", font = ("impact", 25))
style.configure("TFrame", background = "#C0C0C0")
style.configure("TButton", background = "white", font=("Impact", 20), width = 15)

check = (window.register(is_valid), "%P")
radio = IntVar()

frame = Frame(window)
frame.pack(fill=BOTH, side=LEFT, expand=True)

word1 = Label(window, text="Формат")
word1.place(x=35, y=25)
rbt1 = ttk.Radiobutton(window, variable=radio, text="9 x 12", value=1)
rbt1.place(x=35, y=75)
rbt2 = ttk.Radiobutton(window, variable=radio, text="10 x 15", value=2)
rbt2.place(x=35, y=125)
rbt3 = ttk.Radiobutton(window, variable=radio, text="18 x 24", value=3)
rbt3.place(x=35, y=175)

word2 = Label(window, text="Количество: ")
word2.place(x=35, y=225)
txt1 = Entry(window, font = ("Impact", 25), width = 17, validate = "key", validatecommand = check)
txt1.place(x=250, y=225)

bt = Button(window, text = "ОК",  command = lambda:calculation())
bt.place(x=35, y=300)
txt2 = Entry(window, font = ("Impact", 25), width = 29, state = "readonly")
txt2.place(x=35, y=375)


window.mainloop()