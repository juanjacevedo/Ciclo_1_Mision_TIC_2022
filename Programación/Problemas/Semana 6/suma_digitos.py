'''
Modele mediante una funci ́on matem ́atica y dise ̃ne un programa
recursivo sin cadenas, tuplas o listas que calcule la suma de los d ́ıgitos
que componen un n ́umero natural n. Por ejemplo,
suma digitos(123456) = 21.
'''
'''
a = input()
suma = 0
for i in range(len(a)):
    numero = int(a[i])
    suma += numero
print(suma)
'''

'''
def suma_digitos(n:int):
    n = str(n)
    m = len(n) - 1
    if m == 0:return n
    else:
        siguiente = n[0:m] 
        return int(n[len(n) -1]) + int(suma_digitos(siguiente))
    
print(suma_digitos(123456))
'''

import math
def suma_digitos(n:int):
    digits = int(math.log10(n))+1
    if digits == 1: return n
    else: return n % 10 + suma_digitos(n//10)
print(suma_digitos(123456))
