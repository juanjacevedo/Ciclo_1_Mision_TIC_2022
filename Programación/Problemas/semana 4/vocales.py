'''
Desarrollar un programa que determine si en una lista se encuentra
una cadena de caracteres con dos o m ́as vocales. Si la cadena existe
debe imprimirla y si no existe debe imprimir ’No existe’.
'''

lista = []
l = int(input("Cantidad de elementos a ingresar en la lista: "))

for x in range(l):
    valor = str(input("Ingrese los elementos: "))
    lista.append(valor)

bandera = True
lista2 = []

for i in range(len(lista)):
    contador = 0
    cadena = lista[i].lower().replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace(",","").replace(";","").replace(".","")

    if cadena.count("a") >= 2:
        bandera = False
        lista2.append(lista[i])
    elif cadena.count("a") == 1:
        contador += 1

    if cadena.count("e") >= 2:
        bandera = False
        lista2.append(lista[i])
    elif cadena.count("e") == 1:
        contador += 1

    if cadena.count("i") >= 2:
        bandera = False
        lista2.append(lista[i])
    elif cadena.count("i") == 1:
        contador += 1

    if cadena.count("o") >= 2:
        bandera = False
        lista2.append(lista[i])
    elif cadena.count("o") == 1:
        contador += 1

    if cadena.count("u") >= 2:
        bandera = False
        lista2.append(lista[i])
    elif cadena.count("u") == 1:
        contador += 1

    if contador >= 2:
        lista2.append(lista[i])
        bandera = False

if bandera == False: print("La o las cadenas de texto con más de una vocal son: ", ", ".join(lista2))

if bandera == True: print("No existe")

'''
Corregir porque si la palabra tiene tres o más vocales, imprime dos veces el
resultado (ejemplo: Amanecerá. Lo imprime dos veces)
'''
