print("Ingresa la fila del caballo")
fila = int(input())
print("Ingresa la columna del caballo")
columna = int(input())

posiblesSalidas = []
if (1 <= fila <= 8) and (1 <= columna <= 8):
    #posibles movimientos verticales
    if (fila == 1 or fila == 2) and 2 <= columna <= 7:
        nuevaFila = fila + 2
        nuevaColumna1 = columna+1
        nuevaColumna2 = columna-1
        posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna1)+")")
        posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna2)+")")
    elif (fila == 1 or fila == 2) and (columna == 1 or columna == 8):
        nuevaFila = fila + 2
        if columna == 1:
            nuevaColumna1 = columna+1
            posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna1)+")")
        elif columna == 8:
            nuevaColumna1 = columna-1
            posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna1)+")")

    if (fila == 8 or fila == 7) and 2 <= columna <= 7:
        nuevaFila = fila - 2
        nuevaColumna1 = columna+1
        nuevaColumna2 = columna-1
        posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna1)+")")
        posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna2)+")")
    elif (fila == 8 or fila == 7) and (columna == 1 or columna == 8):
        nuevaFila = fila - 2
        if columna == 1:
            nuevaColumna1 = columna+1
            posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna1)+")")
        elif columna == 8:
            nuevaColumna1 = columna-1
            posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna1)+")")

    if 3 <= fila <= 6 and 2 <= columna <= 7:
        nuevaFila1 = fila + 2
        nuevaFila2 = fila - 2
        nuevaColumna1 = columna + 1
        nuevaColumna2 = columna - 1
        posiblesSalidas.append("("+str(nuevaFila1)+", "+str(nuevaColumna1)+")")
        posiblesSalidas.append("("+str(nuevaFila1)+", "+str(nuevaColumna2)+")")
        posiblesSalidas.append("("+str(nuevaFila2)+", "+str(nuevaColumna1)+")")
        posiblesSalidas.append("("+str(nuevaFila2)+", "+str(nuevaColumna2)+")")
    elif 3 <= fila <= 6 and columna == 1:
        nuevaFila1 = fila + 2
        nuevaFila2 = fila - 2
        nuevaColumna1 = columna + 1
        posiblesSalidas.append("("+str(nuevaFila1)+", "+str(nuevaColumna1)+")")
        posiblesSalidas.append("("+str(nuevaFila2)+", "+str(nuevaColumna1)+")")
    elif 3 <= fila <= 6 and columna == 8:
        nuevaFila1 = fila + 2
        nuevaFila2 = fila - 2
        nuevaColumna1 = columna - 1
        posiblesSalidas.append("("+str(nuevaFila1)+", "+str(nuevaColumna1)+")")
        posiblesSalidas.append("("+str(nuevaFila2)+", "+str(nuevaColumna1)+")")

    #posibles movimientos horizontales

    if (columna == 1 or columna == 2) and 2 <= fila <= 7:
        nuevaColumna = columna + 2
        nuevaFila1 = fila+1
        nuevaFila2 = fila-1
        posiblesSalidas.append("("+str(nuevaFila1)+", "+str(nuevaColumna)+")")
        posiblesSalidas.append("("+str(nuevaFila2)+", "+str(nuevaColumna)+")")
    elif (columna == 1 or columna == 2) and (fila == 1 or fila == 8):
        nuevaColumna = columna + 2
        if columna == 1:
            nuevaFila1 = fila+1
            posiblesSalidas.append("("+str(nuevaFila1)+", "+str(nuevaColumna)+")")
        elif columna == 8:
            nuevaFila2 = fila-1
            posiblesSalidas.append("("+str(nuevaFila2)+", "+str(nuevaColumna)+")")

    if (columna == 8 or columna == 7) and 2 <= fila <= 7:
        nuevaColumna = columna - 2
        nuevaFila1 = fila+1
        nuevaFila2 = fila-1
        posiblesSalidas.append("("+str(nuevaFila1)+", "+str(nuevaColumna)+")")
        posiblesSalidas.append("("+str(nuevaFila2)+", "+str(nuevaColumna)+")")
    elif (columna == 8 or columna == 7) and (fila == 1 or fila == 8):
        nuevaColumna = columna - 2
        if columna == 1:
            nuevaFila = fila+1
            posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna)+")")
        elif columna == 8:
            nuevaFila = fila-1
            posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna)+")")

    if 3 <= columna <= 6 and 2 <= fila <= 7:
        nuevaColumna1 = columna + 2
        nuevaColumna2 = columna - 2
        nuevaFila1 = fila + 1
        nuevaFila2 = fila - 1
        posiblesSalidas.append("("+str(nuevaFila1)+", "+str(nuevaColumna1)+")")
        posiblesSalidas.append("("+str(nuevaFila1)+", "+str(nuevaColumna2)+")")
        posiblesSalidas.append("("+str(nuevaFila2)+", "+str(nuevaColumna1)+")")
        posiblesSalidas.append("("+str(nuevaFila2)+", "+str(nuevaColumna2)+")")
    elif 3 <= columna <= 6 and fila == 1:
        nuevaFila = fila + 1
        nuevaColumna1 = columna + 2
        nuevaColumna2 = columna - 2
        posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna1)+")")
        posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna2)+")")
    elif 3 <= columna <= 6 and fila == 8:
        nuevaFila = fila - 1
        nuevaColumna1 = columna + 2
        nuevaColumna2 = columna - 2
        posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna1)+")")
        posiblesSalidas.append("("+str(nuevaFila)+", "+str(nuevaColumna1)+")")

    print("Fila, Columna")
    print(posiblesSalidas)
else:
    print("Error: Posición inválida.")

