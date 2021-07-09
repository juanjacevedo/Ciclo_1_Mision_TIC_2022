import math #Librería

def area_circulo(r):

    '''
    Input: r es el parametro de la función (un float) y p es una constante
    return: el cuadrado de el valor de r por p
    '''

    p = math.pi
    area = p * (r**2)
    return area

print(area_circulo(4))
print(round(area_circulo(4),2)) #Redondea el valor de la funcion area_circulo a la cantidad de decimales que se le asigne


def area_rectangulo(base,alto):
    area = base * alto
    return area

base = float(input("Ingrese la base a calcular: "))
alto = float(input("Ingrese el alto a calcular: "))


if  base == alto:
    print(area_rectangulo(base,alto))
    print ("El rectangulo ingresado es un cuadrado")
    else:
    print("El area del rectangulo es: ", area_rectangulo(base,alto))
