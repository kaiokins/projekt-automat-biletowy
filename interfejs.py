import biletomat
from tkinter import Label, Tk, Button
from oprogramowanie import pieniadze as p
from oprogramowanie import bilet as b
from wyjatki import wyjatki as w

biletomat = biletomat.Biletomat()
print(biletomat.suma())


def action():
    print("Siema")


root = Tk()
root.geometry("600x400")

label = Label(root, text="Automat biletowy MPK", font=30)
label.pack()

test_button = Button(root, text="Klinij", width=8, command=action)
test_button.pack()

root.mainloop()
