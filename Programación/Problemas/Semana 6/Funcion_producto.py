'''
Dise ̃ne un modelo matem ́atico que permita calcular la funci ́on producto,
es decir, que reciba dos (2) n ́umeros naturales y retorne la multiplicaci ́on
del primer n ́umero por el segundo.
No se pueden utilizar los operadores de multiplicaci ́on ni de divisi ́on (ni
entera ni real).
Codifique el modelo matem ́atico utilizando el lenguaje Python.
'''


def producto(a,b):
    try:
        a, b = int(a), int(b)
        if a < 0 or b <0: a/0 #Esta línea de código es por si ingresa un número negativo (no natural)
        if a == 0 or b == 0: return 0
        elif b == 1: return a 
        elif a == 1: return b
        else: return a + producto(a,b-1)
    except:
            return str("No ha ingresado números naturales")


list = input("Ingrese lus números a multiplicar separados por un espacio: ").split()
print(producto(list[0],list[1]))
# try:
#     print(producto(1,4,3))
# except: 
#     print("Ha ingresado más de dos números")