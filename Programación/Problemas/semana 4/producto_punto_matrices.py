'''
Desarrollar un algoritmo que permita multiplicar dos matrices de
n ́umeros reales (enteros).
'''
matriz1 = []
matriz2 = []
matriz3 = []
print("Tamaño de la primer matriz a multiplicar: ")

f1 = int(input("Número de filas: "))
c1 = int(input("Número de columnas: "))

print("Tamaño de la segunda matriz a multiplicar: ")

f2 = int(input("Número de filas: "))
c2 = int(input("Número de columnas: "))

if c1 != f2:
    print("No es posible multiplicar estas dos matrices")
else:
    print("Datos matriz 1: ")
    for i in range(f1):
        matriz1.append([])
        for j in range(c1):
            matriz1[i].append(float(input("ingrese el dato de la posición " + str(i) + "," + str(j) +": " )))

    print("Datos matriz 2: ")
    for i in range(f2):
        matriz2.append([])
        for j in range(c2):
            matriz2[i].append(float(input("ingrese el dato de la posición " + str(i) + "," + str(j) +": " )))

    for i in range(f1):
        matriz3.append([])
        for j in range(c2):
            suma = 0
            for k in range(len(matriz3)):
                producto = matriz1[i][k]*matriz2[k][j]
                suma += producto
            matriz3[i].append(suma)
    print(matriz3)
#TODO:Hay que corregir el código, no da el resultado correcto