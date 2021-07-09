'''
Dada una cadena de longitud 1, determine si el codigo ASCII de
primera letra de la cadena es par o no. Ayuda: utilice la funcion
ord(<caracter>) de Python que retorna el codigo ASCII de una
cadena de longitud 1.
'''

cadena = str(input("Ingrese un carácter: "))
a = int(ord(cadena))


if a%2 == 0:
    print("El código ASCII del carácter ingresado es par")

if a%2 == 1:
    print("El código ASCII del carácter ingresado es impar")
