'''
Dado un caracter, construya un programa en Python para determinar
si el caracter es un dgito o no.
'''

def digito(a):
    if a >= 48 and a <= 57: return str("El carácter ingresado es un dígito")
    else: return str("El carácter ingresado no es un dígito")
print(digito(ord(input("Ingrese un carácter: "))))
