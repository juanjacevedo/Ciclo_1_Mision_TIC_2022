'''
Desarrollar un algoritmo que calcule el producto punto de dos arreglos
de n ́umeros enteros (reales) de igual tama ̃no. Sean
v = [v0, v1, . . . , vn−1] y w = [w0,w1, . . . ,wn−1] dos arreglos, el
producto de v y w (notado v · w) es el n ́umero:
v0 ∗ w0 + v1 ∗ w1 + · · · + vn−1 ∗ wn−1.
'''

l = int(input("Tamaño de ambos arreglos: "))
arreglo1 = []
arreglo2 = []

for x in range(l):
    valor = int(input("Ingrese un valor para el primer arreglo: "))
    arreglo1.append(valor)

for x in range(l):
    valor = int(input("Ingrese un valor para el segundo arreglo: "))
    arreglo2.append(valor)

print(arreglo1)
print(arreglo2)

contador = 0

for i in range(l):
    contador = contador + arreglo1[i]*arreglo2[i]
print("El producto punto de los dos arreglos es:", contador)
