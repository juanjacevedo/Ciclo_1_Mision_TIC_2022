'''
Modele mediante una funci ́on matem ́atica y dise ̃ne un programa
recursivo sin cadenas, tuplas o listas que retorne el primer d ́ıgito de
un n ́umero natural n (le ́ıdo de izquierda a derecha). Por ejemplo,
primero(86420) = 8.
'''
'''
def primero(n:int):
    l = len(str(n))
    if l == 1: return n
    else: return primero(n // 10)
print(primero(86420))
'''

import math
def primero(n:int):
    digits = int(math.log10(n))+1
    if digits == 1: return n
    else: return primero(n // 10)
print(primero(86420))
