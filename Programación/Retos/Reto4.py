'''
La señora María, cliente fiel de la tienda de don Chepe, lleva un listado con los nombres de los productos que comprará como provisión de la semana. En la tienda, cada producto disponible al cliente tiene asociado y visible, su correspondiente nombre de producto y precio.

La señora María requiere ayuda de un programa que, de acuerdo con su listado, le ayude a verificar cuales productos de los que ella requiere están disponibles en la tienda y cuál será su costo total.



Entrada

Como entrada se debe capturar en formato ‘.JSON’, los todos los nombres y precios de los productos que están disponibles para la venta en la tienda. En la siguiente línea se debe capturar el listado de nombres de productos separados por un espacio que se requiere comprar.

Salida

Una línea, con un número que represente el valor total de compra proyectado, de acuerdo con la coincidencia de los productos consultados por la cliente, y en la siguiente línea el nombre de los correspondientes nombres de productos disponibles en la tienda (separados por un espacio).
'''

import  json
json_string = input() #{"pan": 2347, "ajo": 12922, "mango": 2354, "coco": 14132, "arroz": 5863}
data = json.loads(json_string)
listado = input().split() #pasta mango arroz papa pera
contador = 0
lista = []
for producto in listado:
    if producto in data:
        lista.append(producto)
        contador = contador + data[producto]
print(contador)
print(" ".join(lista))


#TODO: Código opcional:
'''
data,codigos= json.loads(input("Ingresa los datos: ")),input("Codigos para verificar: ").split(" ")
perso,suma = codigos.copy(),0
for personas in codigos:
    if personas in data: suma+= data.get(personas,0)
    else:  perso.remove(personas)
print(str(suma) + "\n" + " ".join(perso))
'''