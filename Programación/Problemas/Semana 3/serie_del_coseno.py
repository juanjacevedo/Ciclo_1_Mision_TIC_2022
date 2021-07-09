'''Dise~nar una funcion que permita calcular una aproximacion de la
funcion coseno alrededor de 0 para cualquier valor x 2 R (x dado en
radianes), utilizando los primeros n terminos de la serie de Maclaurin'''

def factorial(a):
    x = 2
    n = 1
    for secuencia in range(1, a + 1, 1):
        x = n * (x - 1)
        n += 1
        x += 1
    return (x - 1)

def cos(x, n):
    suma = 0
    for i in range(0, n + 1, 1):
        serie = (((-1) ** i) * (x ** (2 * i))) / factorial(2 * i)
        suma = serie + suma
    return suma

print(cos(1,15))
