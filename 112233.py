import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random
window = Tk()
window["bg"] = "#fafafa"
window.title("(^^)")
window.wm_attributes("-alpha", 2)
window.geometry("300x250")


def btn_click():
    #messagebox.showinfo('Error', '404')
    print("Artur idiot")
    bth1.place(x= random.randint(0,300), y = random.randint(0,250))


frame = Frame(window, bg='red')
frame.place(relwidth=1, relheight=0.5)

bth1 = Button(frame, text="ffffffffff", bg="green", command=btn_click)
window.geometry("10x10")
bth1.pack()

window.mainloop()
