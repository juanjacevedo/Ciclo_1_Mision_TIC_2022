'''
Desarrollar un programa que dadas dos listas determine que
elementos tiene la primer lista que no tenga la segunda lista.
'''
lista1 = []
l1 = int(input("Ingrese la cantidad de elementos a ingresar en la primer lista: "))
for x in range(l1):
    valor1 = input("Ingrese un valor: ")
    lista1.append(valor1)

lista2 = []
l2 = int(input("Ingrese la cantidad de elementos a ingresar en la segunda lista: "))
for x in range(l2):
    valor2 = input("Ingrese un valor: ")
    lista2.append(valor2)

print(lista1)
print(lista2)

lista3 = []
for i in range(l1):
    if lista1[i] not in lista2:
        lista3.append(lista1[i])

print(lista3)
