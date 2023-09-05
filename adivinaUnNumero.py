

from random import randrange

i = False
mayor = 100
menor = 0
intentos = 0
aleatorio = randrange(mayor+1)
while i != True:
    print("Ingresa un numero entre "+str(menor)+" y "+str(mayor))
    intento = int(input())
    if intento == aleatorio:
        print("Adivinaste! Fueron "+str(intentos)+" intentos")
        i = True
    elif intento > aleatorio:
        mayor = intento
        intentos = intentos + 1
        print("Ménos")
    elif intento < aleatorio:
        menor = intento
        intentos = intentos + 1
        print("Más")

print("Fin del juego...")