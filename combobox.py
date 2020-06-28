from tkinter import *
from tkinter import ttk
def combo():
    v=Tk()

    combo=ttk.Combobox(v)
    combo.place(x=50,y=100)
    combo['values']=('Paracetalo','nastiflu','panadol')

    v.geometry("300x300")
