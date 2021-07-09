'''
Hacer un algoritmo que deje al final de un arreglo de n ́umeros todos
los ceros que aparezcan en dicho arreglo.
'''

arreglo = []
arreglo2 = []
l = int(input("Ingrese el tamaño del arreglo: "))

for c in range(l):
    valor = float(input("Ingrese un valor: "))
    arreglo.append(valor)


while 0.0 in arreglo:
    arreglo.remove(0.0)
    arreglo2.append(0.0)
print(arreglo + arreglo2)
