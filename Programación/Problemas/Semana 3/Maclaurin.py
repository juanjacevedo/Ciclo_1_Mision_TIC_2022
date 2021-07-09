'''Dise~nar una funcion que permita calcular una aproximacion de la
funcion exponencial alrededor de 0 para cualquier valor x E R (x pertenece a los reales),
utilizando los primeros n terminos de la serie de Maclaurin (Función exponencial e^x)'''

def factorial(a):
    x = 2
    n = 1
    for secuencia in range(1, a + 1, 1):
        x = n * (x - 1)
        n += 1
        x += 1
    return (x - 1)

def serieMaclaurin(x, n):
    suma = 0
    for i in range(0, n + 1, 1):
        serie = (x**i)/factorial(i)
        suma = serie + suma
    return(suma)

print(serieMaclaurin(2,1))
