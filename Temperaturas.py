cuenta=1
last3=[0,0,0]
i=1
while True:
    temp=float(input(f"Ingrese temperatura{i}:"))
    if 35<= temp <=50:
        i=i+1
        last3[2]=last3[1]
        last3[1]=last3[0]
        last3[0]=temp
        suma=0
        for j in last3:
            suma=suma+j
        avg=suma/3
        if avg>37:
            print("Temperatura elevada, comuniquese al 113. Promedio de las ultimas 3 revisiones")
            if 37<avg<38:
                print("Alerta Verde")
            elif 38<=avg<=40:
                print("Alerta ámbar")
            else:
                print("Alerta Roja")
    else:
        print("Temperatura fuera de rango")