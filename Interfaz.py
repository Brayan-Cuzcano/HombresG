<<<<<<< HEAD
from tkinter import *
=======
>>>>>>> cb9688e4e95edd783806f4ddaca048cc5a1d14ff
import tkinter as tk
from tkinter import messagebox

lista = []

def guardar():
    n =nombre.get()
    ap=app.get()
    am=apm.get()
    c=correo.get()
    t=telefono.get()
    lista.append(n+"$"+ap+"$"+am+"$"+c+"$"+t)
    escribirContacto()
    messagebox.showinfo("Guardado","Pasiente guardado")
    nombre.set("")
    app.set("")
    telefono.set("")
    correo.set("")
    consultar()
def eliminar():
    eliminado=conteliminar.get()
    removido=False
    for elemento in lista:
        arreglo=elemento.split("$")
        if conteliminar.get()==arreglo[3]:
            lista.remove(elemento)
            removido=True
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado"+eliminado)
def consultar():
    r=Text(ventana,width=80,height=15)
    lista.sort()
    valores=[]
    r.insert(INSERT,"Nombre\t\tApellido P\tApellido M\t\tTelefono\t\tcorreo\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[3])
        r.insert(INSERT,arreglo[0]+"\t\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
    r.place(x=20,y=230)
    if lista==[]:
        spinTelefono=Spinbox(ventana,value=(valores)).place(x=450,y=50)
    r.config(state=DISABLED)
def iniciarArchivo():
    archivo=open("ag.txt","a")
    archivo.close()
def cargar():
    archivo=open("ag.txt","r")
    linea=archivo.readline()
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea=linea[:-1]
            lista.append(linea)
            linea=archivo.readline()
        archivo.close()
def escribirContacto():
    archivo=open("ag.txt","w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento +"\n")
    archivo.close()
    


ventana =Tk()
nombre=StringVar()
app=StringVar()
apm=StringVar()
correo=StringVar()
telefono=StringVar()
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
etiquetaTitulo =Label(ventana,text="Bienvenidos",bg=colorFondo,fg=colorLetra,font=("Helvetica",16)).place(x=230,y=10)
etiquetaN = Label(ventana,text="Nombre: ",bg=colorFondo,fg=colorLetra).place(x=50,y=50)
cajaN = tk.Entry(ventana,textvariable=nombre).place(x=150,y=50)
etiquetaApp = Label(ventana,text="Apellido Paterno: ",bg=colorFondo,fg=colorLetra).place(x=50,y=80)

<<<<<<< HEAD
cajaApp =tk.Entry(ventana,textvariable=app).place(x=150,y=80)
etiquetaApm = Label(ventana, text="Apellido Materno: ",bg=colorFondo,fg=colorLetra  ).place(x=50,y=110)
cajaApm = tk.Entry(ventana, textvariable=apm).place(x=150, y=110)
etiquetaT = Label(ventana,text="Telefono: ",bg=colorFondo,fg=colorLetra).place(x=50,y=140)
cajaT = tk.Entry(ventana,textvariable=telefono).place(x=150,y=140)
etiquetaC = Label(ventana, text="Correo: ", bg=colorFondo, fg=colorLetra).place(x=50,y=170)
cajaC=tk.Entry(ventana,textvariable=correo).place(x=150,y=170)
etiquetaEliminar = Label(ventana, text="Telefono: ",bg=colorFondo,fg=colorLetra).place(x=370,y=50)
spinTelefono = Spinbox(ventana,textvariable=conteliminar).place(x=450,y=50)
botonGuardar= Button(ventana,text="Guardar",command=guardar,bg="#009",fg="White").place(x=180,y=200)
botonEliminar=Button(ventana,text="Eliminar",command=eliminar,bg="#009",fg="White").place(x=470,y=80)
=======
#Va a funcionar como banner pricipal
main_title =tk.Label(ventana,text="Bienvenidos",width=111,height=2)
main_title.place(x=7,y=0)

#Esto va a funcionar como etiquetas cualquiera
Edad_label=tk.Label(text="Nombre de usuario : ", bg="white")
Edad_label.place(x=20, y=70)
#etiquetaN = Label(ventana,text="Nombre: ",bg=colorFondo,fg=colorLetra).place(x=50,y=50)
#cajaN = Entry(ventana,textVariable=nombre).place(x=150,y=50)
#etiquetaApp = Label(ventana,text="Apellido Paterno: ",bg=colorFondo,fg=colorLetra).place(x=50,y=80)
#cajaApp = Entry(ventana,textVariable=app).place(x=150,y=110)
#etiquetaApm = Label(ventana, text="Apellido Materno: ",bg=colorFondo).place(x=50,y=110)
#cajaApm = Entry(ventana, textVariable=apm).place(x=150, y=110)
#etiquetaT = Label(ventana,text="Telefono: ",bg=colorFondo,fg=colorLetra).place(x=140,y=140)
#cajaT = Entry(ventana,textVariable=telefono).place(x=150,y=110)
#etiquetaC = Label(ventana, text="Correo: ", bg=colorFondo, fg=colorLetra).place(x=50,y=80)
#cajaC=Entry(ventana,textVariable=correo).place(x=150,y=170)
#etiquetaEliminar = Label(ventana, text="Telefono: ",bg=colorFondo,fg=colorLetra).place(x=370,y=50)
#spinTelefono = SpingBox(ventana,textVarriable=conteneliminar).place(x=450,y=50)
#botonGuardar= Button(ventana,text="Guardar",command=guardar,bg="#009",fg="White").place(x=180,y=200)
>>>>>>> cb9688e4e95edd783806f4ddaca048cc5a1d14ff
ventana.mainloop()