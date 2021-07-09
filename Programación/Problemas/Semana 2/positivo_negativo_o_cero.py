'''
Dado un numero real x, construya una funcion que permita
determinar si el numero es positivo, negativo o cero. Para cada caso
de debe imprimir el texto que se especica a continuacion:
Positivo: \El numero x es positivo"
Negativo: \El numero x es negativo"
Cero (0): \El numero x es el neutro para la suma"
'''

def negativoPositivoCero(n):
    if n < 0:
        return str("El número ingresado es negativo")
    if n > 0:
        return str("El número ingresado es positivo")
    if n == 0:
        return str("El número ingresado es el neutro para la suma")

n = float(input("Ingrese un número real: "))
print(negativoPositivoCero(n))
