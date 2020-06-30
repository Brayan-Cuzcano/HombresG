#importo el tkinter para la creacion de la interfaz grafica
from tkinter import *

 
# defino unas variables para el envio de informacion
def send_data():
  username_info = username.get()
  password_info = password.get()
  fullname_info = fullname.get()
  print(username_info,"\t", password_info,"\t", fullname_info,"\t")
 
# este codigo abre y escribe en el blog de notas
  file = open("user.txt", "a")
  file.write(username_info)
  file.write("\t")
  file.write(password_info)
  file.write("\t")
  file.write(fullname_info)
  file.write("\t")
  file.close()
  print(" New user registered. Username: {} | FullName: {}   ".format(username_info, fullname_info))
 
#  Borra un dato preevio
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  fullname_entry.delete(0, END)

# Creo una nueva intancia para el TK
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("|Registro de usuarios|")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Registro de datos", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

# creo labels para la interfaz
username_label = Label(text = "Username", bg = "#FFEEDD")
username_label.place(x = 290, y = 70)
password_label = Label(text = "Password", bg = "#FFEEDD")
password_label.place(x = 290, y = 130)
fullname_label = Label(text = "Fullname", bg = "#FFEEDD")
fullname_label.place(x = 290, y = 190)
 
# obtienen datos de los usuarios
username = StringVar()
password = StringVar()
fullname = StringVar()
 
username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40",  show = "*")
fullname_entry = Entry(textvariable = fullname, width = "40")
 

#con este codigo estoy pocicionando los recuadros.
username_entry.place(x = 200, y = 100)
password_entry.place(x = 200, y = 160)
fullname_entry.place(x = 200, y = 220)
 
# creacion de botones
submit_btn = Button(mywindow,text = "Guardar", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 222, y = 290)



#abrir cuado principal
mywindow.mainloop()