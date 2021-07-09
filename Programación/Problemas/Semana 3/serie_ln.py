'''Dise~nar una funcion que permita calcular una aproximacion de la
funcion logaritmo natural alrededor de 0 para cualquier valor x 2 R+,
utilizando los primeros n terminos de la serie de Maclaurin'''

def ln(x, n):
    suma = 0
    for i in range(0, n + 1, 1):
        serie = (1 / (2*i + 1)) * (((x**2) - 1)/((x**2) + 1)) ** (2*i + 1)
        suma = serie + suma
    return suma

print(ln(2,15))
