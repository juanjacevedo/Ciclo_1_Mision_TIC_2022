'''
Desarrollar un algoritmo que calcule el promedio de un arreglo de
reales.
'''

lista = []
l = int(input("Ingresar el tamaño del arreglo: "))

for x in range(l):
    valor = float(input("Ingrese un valor: "))
    lista.append(valor)

contador = 0

for i in range(l):
    contador = contador + lista[i]
promedio = contador/len(lista)

print(lista)
print("El promedio es:", promedio)
