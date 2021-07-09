'''
Desarrollar un algoritmo que calcule el producto directo de dos
arreglos de n ́umeros reales de igual tama ̃no. Sean
v = [v0, v1, . . . , vn−1] y w = [w0,w1, . . . ,wn−1] dos arreglos, el
producto directo de v y w (notado v ∗ w) es el vector:
[v0 ∗ w0, v1 ∗ w1, . . . , vn−1 ∗ wn−1].
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

arreglo3 = []

for i in range(l):
    valor = arreglo1[i] * arreglo2[i]
    arreglo3.append(valor)

print(arreglo1)
print(arreglo2)
print(arreglo3)
