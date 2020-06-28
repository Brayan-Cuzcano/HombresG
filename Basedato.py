lista=[]
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