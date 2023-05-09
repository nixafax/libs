from tkinter import *
from tkinter import ttk

price = 0.25
cof = {"пластик": 1, "алюминий": 2.3, "соломка": 0.8, "текстиль": 1.5}

def dot(newval):
    if "." in newval:
        return True
    else:
        return False

def is_valid(newval):
    return newval == "" or (newval.isnumeric() or dot(newval))

def calculation():
    vl1 = txt1.get()
    vl2 = txt2.get()
    if vl1 == "" or vl2 == "" or combo.get() == "":
        txt3["state"] = "normal"
        txt3.delete(0, END)
        txt3.insert(0, "Сначала введите данные")
        txt3["state"] = "readonly"
    else:
        vl3 = cof[combo.get()]
        ot = "Итоговая цена: " + str(float(vl1)*float(vl2)*vl3*price) + " руб."
        txt3["state"] = "normal"
        txt3.delete(0, END)
        txt3.insert(0, ot)
        txt3["state"] = "readonly"

window = Tk()
window.title("Жалюзи")
window.geometry("600x350")

check = (window.register(is_valid), "%P")

frame = Frame(window, bg = "#C0C0C0")
frame.pack(fill=BOTH, side=LEFT, expand=True)

word1 = Label(window, text = "Ширина (см.)", font = ("Impact", 25), bg = "#C0C0C0")
word1.place(x=35, y=25)
txt1 = Entry(window, font = ("Impact", 25), width = 17, validate = "key", validatecommand = check)
txt1.place(x=250, y=25)
word2 = Label(window, text = "Высота (см.)", font = ("Impact", 25), bg = "#C0C0C0")
word2.place(x=35, y=75)
txt2 = Entry(window, font = ("Impact", 25), width = 17, validate = "key", validatecommand = check)
txt2.place(x=250, y=75)
word3 = Label(window, text = "Материал", font = ("Impact", 25), bg = "#C0C0C0")
word3.place(x=35, y=125)
combo = ttk.Combobox(window, values = ("пластик", "алюминий", "соломка", "текстиль"), font=("Impact", 25), width = 16, state = "readonly")
combo.place(x=250, y=125)

bt = Button(window, text = "ОК", font = ("Impact", 15), width = 15, height = 1, command =lambda:calculation())
bt.place(x=35, y=200)
txt3 = Entry(window, font = ("Impact", 25), width = 29, state = "readonly")
txt3.place(x=35, y=275)


window.mainloop()