'''Desarrollar un programa que determine si un elemento de una lista es
una cadena pal ́ındrome. Si la cadena existe debe imprimirla y si no
existe debe imprimir ’No existe’.'''
lista = []
l = int(input("Cantidad de elementos a ingresar en la lista: "))
for x in range(l):
    valor = str(input("Ingrese los elementos:"))
    lista.append(valor)
lista2 = []
bandera = True
for i in range(len(lista)):
    list = lista[i].lower().replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace(",","").replace(";","").replace(".","")
    palabra = list[::-1]
    if list == palabra:
        lista2.append(lista[i])
        bandera = False
if bandera == False: print("La o las cadenas de texto palindromas son: ", ", ".join(lista2))
if bandera == True: print("No existe")
