'''
1) Establezca el modelo matemático (función matemática) que permita calcular lateral del vagón.
2) Escriba una función en Python que implemente la función anteriormente modelada, en la cual se invoque la constante matemática π del módulo math.
'''

import math

def area_circulo(radio):
    pi = math.pi
    return pi * radio**2

def area_rectangulo(base, altura):
    return base * altura

def area_vagon(radio, base, altura):
    return 2 * area_circulo(radio) + area_rectangulo(base, altura)

radio = float(input("Ingrese el valor del radio de los circulos: "))
base = float(input("Ingrese el valor de la base del vagón: "))
altura = float(input("Ingrese el valor de la altura del vagón: "))

print("El valor del area latera del vagón es: ", round(area_vagon(radio, base, altura), 2))
