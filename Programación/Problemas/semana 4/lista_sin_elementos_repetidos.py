'''Desarrollar un programa que determine si en una lista no existen
elementos repetidos.'''


lista=[]
l = int(input("Cantidad de elementos a ingresar en la lista: "))
for x in range(l):
    valor = input("Ingrese los elementos:")
    lista.append(valor)
bandera = True
for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] == lista[j]:
            bandera = False

if bandera == False: print("Hay elementos repetidos")
if bandera == True: print("No hay elementos repetidos")
