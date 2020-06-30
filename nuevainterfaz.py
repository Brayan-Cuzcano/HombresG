#Importamos librerias como tkinter , modulos los cuales van a ayudar como ventanas secundarias,
#y por ultimo para manera mas estetica , hemos importado un datetime , para que aparesca en un
#cuadro la fecha actual.

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from secundario import nuevo
from datetime import date


lista = []

#definimos una funcion la cual va a servir mas adelante en el boton de guardar
def guardar():
    #llamamos a distintas
    Fecha=e2.get()
    n =nombre.get()
    ap=app.get()
    am=medicamento.get()
    c=temperatura.get()
    
    lista.append(n+"$"+ap+"$"+am+"$"+c+"$"+Fecha)
    escribirContacto()
    messagebox.showinfo("Guardado","Pasiente guardado")

    #al momento de presionar el boton , el codigo de abajo reseteara los recuadros.
    nombre.set("")
    app.set("")
    temperatura.set("")
    medicamento.set("")
    consultar()

#Defino el boton de eliminar    
def eliminar():
    eliminado=conteliminar.get()
    removido=False
    for elemento in lista:
        arreglo=elemento.split("$")
        lista.remove(elemento)
            
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado"+eliminado)
def calculareT():
    nuevo()

def consultar():
    r=Text(ventana,width=80,height=15)
    lista.sort()
    valores=[]
    r.insert(INSERT,"Nombre\t\tApellido \t\tMedicamento\t\tTemperatura \t\tfecha(dd/mm/aa)\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[3])
        r.insert(INSERT,arreglo[0]+"\t\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
    r.place(x=20,y=230)
#Defino una funcion , lo que me servira para el blog de notas , donde estara almacenando mis
#datos.
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
nombre=StringVar()
app=StringVar()
medicamento=StringVar()
Fecha=StringVar()
temperatura=StringVar()
conteliminar=StringVar()

cargar()
iniciarArchivo()
consultar()

#Creacion de Ventana
colorFondo="#006"
colorLetra="#FFF"
ventana.title("Interfaz Grafica - HombreG productions :v")
ventana.geometry("700x500")
ventana.configure(background=colorFondo)

#Etiquetas Creacion
etiquetaTitulo =Label(ventana,text="Registro | #Quedate en Casa ",bg=colorFondo,fg=colorLetra,font=("Helvetica",16)).place(x=230,y=10)
#Nombre
etiquetaN = Label(ventana,text="Nombre: ",bg=colorFondo,fg=colorLetra).place(x=50,y=50)
cajaN = tk.Entry(ventana,textvariable=nombre).place(x=150,y=50)
#Apellido
etiquetaAp = Label(ventana,text="Apellido: ",bg=colorFondo,fg=colorLetra).place(x=50,y=80)
cajaAp =tk.Entry(ventana,textvariable=app).place(x=150,y=80)
#Medicamiento
etiquetamed = Label(ventana, text="Medicamento: ",bg=colorFondo,fg=colorLetra  ).place(x=50,y=110)
cajamed = tk.Entry(ventana, textvariable=medicamento).place(x=150, y=110)
#Temperatura
etiquetaT = Label(ventana,text="Temperatura: ",bg=colorFondo,fg=colorLetra).place(x=50,y=140)
cajaT = tk.Entry(ventana,textvariable=temperatura).place(x=150,y=140)

#Fecha
etiquetaF = Label(ventana, text="Fecha: ", bg=colorFondo, fg=colorLetra).place(x=50,y=170)
e2 = tk.Entry(ventana)
#Utilizamos el modulo de date time en el cuadro
today = date.today()
Fecha = str(today.day) + "-" + str(today.month) + "-" + str(today.year)
e2.insert(10, Fecha)
e2.place(x=150,y=170)
#Creacion de los botones : Guardar , Eliminar y Calcular Temperaturas
botonGuardar= Button(ventana,text="Guardar",command=guardar,bg="#009",fg="White").place(x=180,y=200)
botonEliminar=Button(ventana,text="Eliminar",command=eliminar,bg="#009",fg="White").place(x=470,y=200)
botonCalcular=Button(ventana,text="Calcular temperaturas",command=calculareT,bg="#009",fg="White").place(x=470,y=110)
ventana.mainloop()