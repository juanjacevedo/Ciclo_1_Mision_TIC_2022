'''
1) Establezca el modelo matemático (función matemática) que permita calcular el
volumen del sólido anteriormente mostrado.
2) Escriba una función en Python que implemente la función anteriormente modelada,
en la cual se invoque la constante matemática π del módulo math.
3) Para los valores r1 = 3, h = 9/2 y r2 = 4, calcule (a mano o con calculadora)
el volumen del sólido y compárelo con el resultado obtenido  a partir de la
evaluación de la función anteriormente implementada. ¿Qué pasa si se invoca la
función con los mismos valores, pero h se calcula como la expresión  h = 9//2?
'''
import math

def volumen_cono(radio, altura):
    pi = math.pi
    return (1/3)*altura*pi*radio**2

def volumen_esfera(radio):
    pi = math.pi
    return (4/3)*pi*radio**3

def volumen_solido(radio_esfera,radio_cono,altura_cono):
    return volumen_esfera(radio_esfera) + volumen_cono(radio_cono,altura_cono)

radioEsfera = float(input("Ingrese r1: "))
radioCono = float(input("Ingrese r2: "))
alturaCono = float(input("Ingrese h: "))

print("El valor del volumen del sólido, es: ", round(volumen_solido(radioEsfera, radioCono, alturaCono), 2))
