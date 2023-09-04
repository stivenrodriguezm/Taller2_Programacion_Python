

print("Ingresa un número entero:")
numero = input()

array1 = []
array2 = []

for i in numero:
    array1.append(i)

cantidad = len(array1)
index = cantidad
for i in array1:
    index = index - 1
    valor = str(array1[index])
    array2.append(valor)


if array1 == array2:
    print(str(numero)+" es un número Palindromo")
else:
    print(str(numero)+" no es un número palindromo")