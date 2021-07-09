'''
Desarrollar un algoritmo que determine si una cadena de caracteres es
pal ́ındrome. Una cadena se dice pal ́ındrome si al invertirla es igual a
ella misma.
'''

a = input("Ingrese una cadena: ")
b = a[::-1]
if a == b:
    print("Es palindromo")
else:
    print("No es palindromo")
