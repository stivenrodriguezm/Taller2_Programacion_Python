
valor = 1
positivos = []
negativos = []
while valor != 0:
    print("Ingresa un valor entero:")
    valor = int(input())
    if valor > 0:
        positivos.append("*")
    if valor < 0:
        negativos.append("*")

print("Positivos: ", end=" ")
for i in positivos:
    print(str(i), end=" ")

print("\nNegativos: ", end=" ")
for i in negativos:
    print(str(i), end=" ")