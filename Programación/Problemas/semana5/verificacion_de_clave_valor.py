'''
Desarrollar un algoritmo que verifique si todas las clave:valor de
un diccionario se encuentran en otro diccionario.
'''

punto1 = {'x': 2, 'y': 1, 'z': 4}
punto2 = {'a': 3, 'b': 5, 'z': 4}
punto3 = {'x': 2, 'y': 1, 'z': 4}

def uno_en_otro(diccionario1, diccionario2):
    
    if diccionario1.items() == diccionario2.items():
        resultado = str("Todas las claves:valor se encuentran en el otro diccionario")
    else:
        resultado = str("No todas las claves:valor se encuentran en el otro diccionario")
    return resultado

print(uno_en_otro(punto1,punto2))
print(uno_en_otro(punto1,punto3))