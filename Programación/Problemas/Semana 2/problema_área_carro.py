'''
1) Establezca el modelo matemático (función matemática) que permita calcular el área del carro
2) Escriba una función en Python que implemente la función matemática previamente modelada,
en la cual se utilice la composición de las funciones de suma de números reales, area_circulo y area_rectangulo
codficadas previamente
'''

import math

def area_circulo(radio):
    pi = math.pi
    return pi * radio**2

def area_rectangulo(base, altura):
    return base * altura

def area_carro (radio1, radio2, base1, altura1, base2, altura2):
    area = area_circulo(radio1) + area_circulo(radio2) + area_rectangulo(base1, altura1) + area_rectangulo(base2, altura2)
    return area

radio1 = float(input("Ingrese el valor de r1: "))
radio2 = float(input("Ingrese el valor de r2: "))
base1 = float(input("Ingrese el valor de b1: "))
altura1 = float(input("Ingrese el valor de a1: "))
base2 = float(input("Ingrese el valor de b2: "))
altura2 = float(input("Ingrese el valor de a2: "))

print("El valor de el área lateral del carro, es: ", round(area_carro(radio1, radio2, base1, altura1, base2, altura2), 2))
