from tkinter import *
from tkinter import messagebox

lista = []

def guardar():
    print("Hola")

ventana = Tk()
nombre = StringVar()
app=StringVar()
apm=StringVar()
correo = StringVar()
telefono=StringVar()
conteliminar=StringVar()
colorFondo="#006"
colorLetra="#FFF"
ventana.title("Agenda con archivos")
ventana.geometry("800x500")
ventana.configure(background=colorFondo)
etiquetaTitulo = Label(ventana,text="Agenda con Archivos",bg=colorFondo,fg=colorLetra,font=("Helvetica",16)).place(x=230,y=10)
etiquetaN = Label(ventana,text="Nombre: ",bg=colorFondo,fg=colorLetra).place(x=50,y=50)
cajaN = Entry(ventana,textVariable=nombre).place(x=150,y=50)
etiquetaApp = Label(ventana,text="Apellido Paterno: ",bg=colorFondo,fg=colorLetra).place(x=50,y=80)
cajaApp = Entry(ventana,textVariable=app).place(x=150,y=110)
etiquetaApm = Label(ventana, text="Apellido Materno: ",bg=colorFondo).place(x=50,y=110)
cajaApm = Entry(ventana, textVariable=apm).place(x=150, y=110)
etiquetaT = Label(ventana,text="Telefono: ",bg=colorFondo,fg=colorLetra).place(x=140,y=140)
cajaT = Entry(ventana,textVariable=telefono).place(x=150,y=110)
etiquetaC = Label(ventana, text="Correo: ", bg=colorFondo, fg=colorLetra).place(x=50,y=80)
cajaC=Entry(ventana,textVariable=correo).place(x=150,y=170)
etiquetaEliminar = Label(ventana, text="Telefono: ",bg=colorFondo,fg=colorLetra).place(x=370,y=50)
spinTelefono = SpingBox(ventana,textVarriable=conteneliminar).place(x=450,y=50)
botonGuardar= Button(ventana,text="Guardar",command=guardar,bg="#009",fg="White").place(x=180,y=200)
mainloop()