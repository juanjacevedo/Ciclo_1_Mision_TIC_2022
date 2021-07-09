'''Desarrollar un algoritmo que permita sumar dos matrices de n ́umeros
reales (enteros).'''

matriz1 = []
matriz2 = []
matriz3 = []
print("Tamaño de la primer matriz a sumar: ")

f1 = int(input("Número de filas: "))
c1 = int(input("Número de columnas: "))

print("Tamaño de la segunda matriz a sumar: ")

f2 = int(input("Número de filas: "))
c2 = int(input("Número de columnas: "))

if f1 != f2 or c1 != c2:
    print("No es posible sumar las matrices")
else:
    print("Datos matriz 1: ")
    for i in range(f1):
        matriz1.append([])
        for j in range(c1):
            matriz1[i].append(float(input("ingrese el dato de la posición " + str(i) + "," + str(j) +": " )))

    print("Datos matriz 2: ")
    for i in range(f1):
        matriz2.append([])
        for j in range(c1):
            matriz2[i].append(float(input("ingrese el dato de la posición " + str(i) + "," + str(j) +": " )))


    for i in range(f1):
        matriz3.append([])
        for j in range(c1):
            suma = matriz1[i][j] + matriz2[i][j]
            matriz3[i].append(suma)
    print("Matriz 1: ", end="")
    print(matriz1)
    print("Matriz 2: ", end="")
    print(matriz2)
    print("Resultado de la suma: ", end="")
    print(matriz3)
