'''Desarrollar un programa que dado un n ́umero entero positivo n
calcule e imprima (separados por espacios) n/2 si es par o 3n + 1 si es
impar. El programa debe repetir el proceso con el n ́umero resultado
de dicha operaci ́on mientras este sea diferente de 1. Por ejemplo para
el n ́umero 3 debe imprimir 10 5 16 8 4 2 1.'''

numero = int(input("Ingrese un número entero positivo: "))

while numero <= 0:
    int(input("Ingrese un número entero positivo: "))

while numero > 1:

    if numero % 2 == 0:
        numero = int(numero / 2)

    else:
        numero = int(3*numero + 1)

    print(numero, end =" ")
