'''Desarrollar un programa que imprima el cuadrado del n ́umero que el
usuario ingresa mientras que el n ́umero ingresado no sea negativo.'''

numero = float(input("Ingrese un número positivo: "))

while numero < 0:
    numero = float(input("Ingrese un número positivo: "))

if numero >= 0:
    cuadrado = round(numero**2,2)

print("El cuadrado del numero ingresado es: ", cuadrado)
