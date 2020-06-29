from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import date
import Temperaturas

lista = []

def guardar():
    Temperatura=e1.get()
    Fecha=e2.get()
    
    lista.append(Temperatura+"$"+Fecha)
    escribirContacto()
    messagebox.showinfo("Guardado","Información del paciente a sido guardado.")
    
    consultar()
def eliminar():
    eliminado=conteliminar.get()
    removido=False
    for elemento in lista:
        arreglo=elemento.split("$")
        if (conteliminar.get())==arreglo[0]:
            lista.remove(elemento)
            removido=True
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar","Informacion del paciente a sido eliminado."+eliminado)
def consultar():
    r=Text(ventana,width=80,height=15)
    lista.sort()
    valores=[]
    r.insert(INSERT,"Fecha\t\tTemperatura\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        #valores.append(arreglo[1])
        r.insert(INSERT,arreglo[1]+"\t\t"+arreglo[0]+"\n")
    r.place(x=20,y=130)
    #if lista==[]:
    #    spinTelefono=Spinbox(ventana,value=(valores)).place(x=250,y=20)
    r.config(state=DISABLED)
def iniciarArchivo():
    archivo=open("oh.txt","a")
    archivo.close()
def cargar():
    archivo=open("oh.txt","r")
    linea=archivo.readline()
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea=linea[:-1]
            lista.append(linea)
            linea=archivo.readline()
        archivo.close()
def escribirContacto():
    archivo=open("oh.txt","w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento +"\n")
    archivo.close()
    


ventana =Tk()
Fecha=StringVar()
Temperatura=StringVar()
#app=StringVar()
#apm=StringVar()
#correo=StringVar()
#telefono=StringVar()
conteliminar=StringVar()

cargar()
iniciarArchivo()
consultar()
#Creacion de Ventana

colorFondo="#006"
colorLetra="#FFF"
ventana.title("IMSOMNIA - Hombres G")
ventana.geometry("700x500")
ventana.configure(background=colorFondo)

#Etiquetas Creacion

##etiquetaTitulo =Label(ventana,text="Bienvenidos",bg=colorFondo,fg=colorLetra,font=("Helvetica",16)).place(x=295,y=10)
##etiquetaN = Label(ventana,text="Temperatura : ",bg=colorFondo,fg=colorLetra).place(x=50,y=50)
#cajaN = tk.Entry(ventana,textvariable=nombre).place(x=150,y=50)
##etiquetaApp = Label(ventana,text="Fecha : ",bg=colorFondo,fg=colorLetra).place(x=50,y=80)
#cajaApp =tk.Entry(ventana,textvariable=app).place(x=150,y=80)
##Prue=tk.Entry(ventana.insert(0, "¡Hola, mundo!")).place(x=150,y=80)
#today = date.today()
#print("Today's date:", today)
#Entry.insert(0, "¡Hola, mundo!")

##cajaApp.insert(0,'Hola mundo')

#app="holamundo"
#entry = tk.Entry(ventana)
# Posicionarla en la ventana.
#entry.place(x=150, y=100)



tk.Label(ventana, text="Temperatura").place(x=50,y=80)        #grid(row=0)
tk.Label(ventana, text="Fecha").place(x=50,y=100)         #grid(row=1)
##e1 es temperatura
##e2 es fecha
e1 = tk.Entry(ventana)
e2 = tk.Entry(ventana)

today = date.today()
#recordar
Fecha = str(today.day) + "-" + str(today.month) + "-" + str(today.year)
print("Today's date:", today)
e2.insert(10, Fecha)





e1.place(x=130,y=80)
e2.place(x=130,y=100)













#etiquetaApm = Label(ventana, text="Temperatura 3 : ",bg=colorFondo,fg=colorLetra  ).place(x=50,y=110)
#cajaApm = tk.Entry(ventana, textvariable=apm).place(x=150, y=110)
#etiquetaT = Label(ventana,text="Temperatura 4 : ",bg=colorFondo,fg=colorLetra).place(x=50,y=140)
#cajaT = tk.Entry(ventana,textvariable=telefono).place(x=150,y=140)
#etiquetaC = Label(ventana, text="Temperatura 5 : ", bg=colorFondo, fg=colorLetra).place(x=50,y=170)
#cajaC=tk.Entry(ventana,textvariable=correo).place(x=150,y=170)
#etiquetaEliminar = Label(ventana, text="Telefono: ",bg=colorFondo,fg=colorLetra).place(x=370,y=50)
#spinTelefono = Spinbox(ventana,textvariable=conteliminar).place(x=450,y=50)
botonGuardar= Button(ventana,text="Guardar",command=guardar,bg="#009",fg="White").place(x=280,y=50)
botonEliminar=Button(ventana,text="Eliminar",command=eliminar,bg="#009",fg="White").place(x=300,y=80)
ventana.mainloop()