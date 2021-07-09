'''
Capture la excepcion que evita que el usuario acceda a posiciones que
no se encuentran definidas en la lista dada y muestre el mensaje
Intenta acceder una posicion que no esta en el arreglo:

lista = [1, 2, 3, 4]
lista[5]

Si se ejecuta sin el manejo de la excepcion se produce la siguiente
salida:
IndexError Traceback (most recent call last)
<ipython-input-42-64245f71fd49> in <module>
1 lista = [1, 2, 3, 4]
----> 2 lista[5]
IndexError: list index out of range
'''

try:
    lista = [1,2,3,4]
    print(lista[5])
except:
    print("Intenta acceder una posicion que no esta en el arreglo")

#TODO: Código opcional que funciona de manera general para una lista de tamaño 10 (como máximo) o 0 (como mínimo):
'''
import random
try:
    lista = []
    for i in range(random.randint(0,11)):
        valor = random.randint(0,100)
        lista.append(valor) 
    print(lista)
    posicion = int(input("Ingrese a la posición a la que quiere acceder: "))
    print(lista[posicion-1])
except:
    print("Intenta acceder una posicion que no esta en el arreglo")
'''