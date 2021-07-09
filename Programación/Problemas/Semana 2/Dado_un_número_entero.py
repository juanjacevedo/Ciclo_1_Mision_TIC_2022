'''
Dado un número entero, determinar si ese número corresponde al
código ASCII de una vocal minúscula. Ayuda: utilice la función
chr(<número>) de Python que retorna el carácter ASCII
correspondiente al número entero en el cual se evalúe la función.
'''

def vocalMinuscula(n):
    if n == 97 or n == 101 or n == 105 or n == 111 or n == 117: return chr(n)
    return str("El número ingresado no pertenece a una vocal minúscula en el código ASCII")
print(vocalMinuscula(int(input("Ingrese un número entero: "))))
