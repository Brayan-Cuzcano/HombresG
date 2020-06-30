from tkinter import *
import tkinter as tk


val=int
def nuevo():
    def suma():
        suma=int(entrada1.get())+int(entrada2.get())+int(entrada3.get())
        return suma




#def nuevo():
#    def suma():
#        suma= Temperaturas.temp(entrada1,entrada2,entrada3)
#        return suma

    
    vvt = Tk()
    vvt.title("Calcular temperatura")
    vvt.geometry("400x400")
    vvt.config(bg="#006")
    var=tk.StringVar()
        #titulo
    el=Label(vvt,text="Ingrese temperaturas1",bg="red",fg="black")
    el.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=X)
        #cuadro de entrada para temperatura 1
    entrada1= Entry(vvt)
    entrada1.pack(fill=X,padx=5,pady=5,ipadx=5,ipady=5)
    e2=Label(vvt,text="Ingrese temperaturas2",bg="red",fg="black")
    e2.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=X)
    entrada2= Entry(vvt)
    entrada2.pack(fill=X,padx=5,pady=5,ipadx=5,ipady=5)
    e3=Label(vvt,text="Ingrese temperaturas3",bg="red",fg="black")
    e3.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=X)
    entrada3= Entry(vvt)
    entrada3.pack(fill=X,padx=5,pady=5,ipadx=5,ipady=5)
    #boton de calcular temperatura
    botonsuma=Button(vvt,text="Calcular temperatura",fg="red",command=suma)
    botonsuma.pack(side=TOP)
    res=Label(vvt,bg="plum",textvariable=var,padx=5,pady=5,width=50)
    res.pack()