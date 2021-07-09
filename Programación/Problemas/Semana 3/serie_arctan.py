'''Dise~nar una funcion que permita calcular una aproximacion de la
funcion arco tangente para cualquier valor x 2 [􀀀1; 1], utilizando los
primeros n terminos de la serie de Maclaurin (al evaluar esta funcion
el resultado que se obtiene esta expresado en radianes)'''

def arctan(x, n):
    suma = 0
    for i in range(0, n + 1, 1):
        serie = (-1)**i * x**(2*i + 1) / (2*i +1)
        suma = serie + suma
    return suma

print(arctan(0.5,1))
