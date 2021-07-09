'''
Modele mediante una funci ́on matem ́atica y dise ̃ne un programa
recursivo que calcule la suma de los primeros n cuadrados de los
n ́umeros naturales
'''

def suma_cuadrados(n):
    try:
        if n == 0: return n
        else: return n**2 + suma_cuadrados(n-1)
    except: return str("No ha ingresado un número natural")

print(suma_cuadrados(2))