'''
Desarrollar una funci ́on que reciba dos diccionarios como par ́ametros
y los mezcle, es decir, que se construya un nuevo diccionario con las
llaves de los dos diccionarios; si hay una clave repetida en ambos
diccionarios, se debe asignar el valor que tenga la clave en el
primer diccionario.
'''
punto1 = {'x': 2, 'y': 1, 'z': 4}
punto2 = {'a': 3, 'b': 5, 'z': 3}

def addDict(diccionario1, diccionario2):
    
    for k in diccionario1.keys():
        if k in diccionario2.keys():
            diccionario2.pop(k)
    
    lista1 = list(diccionario1.items())
    lista2 = list(diccionario2.items())

    print(dict(lista1 + lista2))

addDict(punto1, punto2)



