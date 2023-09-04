

tiempo = 1
suma = 0
while tiempo != 0:
    print("Duración tramo:")
    tiempo = int(input())
    if tiempo >=0:
        suma = suma + tiempo
    else:
        print("Ingresa un tiempo válido, en minutos.")

horas = int(suma/60)
minutos = suma % 60

if minutos >= 10:
    print("Tiempo total del viaje: "+str(horas)+ ":"+str(minutos)+" horas")
elif minutos < 10:
    print("Tiempo total del viaje: "+str(horas)+ ":0"+str(minutos)+" horas")
