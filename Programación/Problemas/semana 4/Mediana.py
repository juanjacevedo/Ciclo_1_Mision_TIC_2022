'''
Desarrollar un algoritmo que determine la mediana de un arreglo de
enteros. La mediana es el n ́umero que queda en la mitad del arreglo
despu ́es de ser ordenado.
'''

arreglo = []

l = int(input("Tamaño del arreglo: "))

for c in range(l):
    valor = float(input("Ingrese un valor: "))
    arreglo.append(valor)

arreglo.sort()
n = (l-1)//2

if l % 2 == 0:

    s = arreglo[n] + arreglo[n+1]
    mediana = s/2
    print(arreglo)
    print(mediana)

else:

    mediana = arreglo[n]
    print(arreglo)
    print(mediana)
