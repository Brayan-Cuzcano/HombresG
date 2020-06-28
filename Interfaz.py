from tkinter import * 
import tkinter as tk
from tkinter import messagebox

lista = []

def guardar():
    print("Hola")

ventana =tk.Tk()

#Creacion de Ventana

#colorFondo="#006"
#colorLetra="#FFF"
ventana.title("Interfaz Grafica - HombreG productions :v")
ventana.geometry("800x500")
ventana.configure(bg="black")
ventana.resizable(False,False)


#Etiquetas Creacion

main_title =tk.Label(ventana,text="Bienvenidos",width=111,height=2)
main_title.place(x=7,y=0)
etiquetaN = Label(ventana,text="Nombre: ",bg="#006",fg="#FFF").place(x=50,y=50)
cajaN = Entry(ventana,textVariable="nombre").place(x=150,y=50)
etiquetaApp = Label(ventana,text="Apellido Paterno: ",bg="#006",fg="#FFF").place(x=50,y=80)
cajaApp = Entry(ventana,textVariable="app").place(x=150,y=110)
etiquetaApm = Label(ventana, text="Apellido Materno: ",bg="#006").place(x=50,y=110)
cajaApm = Entry(ventana, textVariable="apm").place(x=150, y=110)
etiquetaT = Label(ventana,text="Telefono: ",bg="#006",fg="#FFF").place(x=140,y=140)
cajaT = Entry(ventana,textVariable="telefono").place(x=150,y=110)
etiquetaC = Label(ventana, text="Correo: ", bg="#006", fg="#FFF").place(x=50,y=80)
cajaC=Entry(ventana,textVariable="correo").place(x=150,y=170)
etiquetaEliminar = Label(ventana, text="Telefono: ",bg="#006",fg="#FFF").place(x=370,y=50)
spinTelefono = messagebox(ventana,textVarriable="conteneliminar").place(x=450,y=50)
botonGuardar= Button(ventana,text="Guardar",command=guardar,bg="#009",fg="White").place(x=180,y=200)
ventana.mainloop()