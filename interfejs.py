import biletomat
from tkinter import *
from oprogramowanie import pieniadze as p
from oprogramowanie import bilet as b
from wyjatki import wyjatki as w

biletomat = biletomat.Biletomat()
print(biletomat.suma())


def action2():
    print("Działa")


root = Tk()
root.title("Automat biletowy MPK")
root.geometry("600x400")

label = Label(root, text="Proszę wybrać rodzaj bilet", font=30)
label.pack()

ulg20b = Button(root, text="20-minutowy ulgowy", command=action2)
ulg20i = Entry(root, width=5)
ulg20b.pack()
ulg20i.pack()

ulg40b = Button(root, text="40-minutowy ulgowy", command=action2)
ulg40i = Entry(root, width=5)
ulg40b.pack()
ulg40i.pack()

ulg60b = Button(root, text="60-minutowy ulgowy", command=action2)
ulg60i = Entry(root, width=5)
ulg60b.pack()
ulg60i.pack()

norm20b = Button(root, text="20-minutowy normalny", command=action2)
norm20i = Entry(root, width=5)
norm20b.pack()
norm20i.pack()

norm40b = Button(root, text="40-minutowy normalny", command=action2)
norm40i = Entry(root, width=5)
norm40b.pack()
norm40i.pack()

norm60b = Button(root, text="60-minutowy normalny", command=action2)
norm60i = Entry(root, width=5)
norm60b.pack()
norm60i.pack()

podsumowanie = Button(root, text="Podsumuj", command=action2)
podsumowanie.pack()

root.mainloop()
