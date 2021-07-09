'''
Modele mediante una funci ́on matem ́atica y dise ̃ne un programa
recursivo sin cadenas, tuplas o listas que dado un n ́umero natural n
inserte un d ́ıgito al comienzo del n ́umero. Por ejemplo,
inserta(7, 654321) = 7654321.
'''
import math
def inserta(n: int, m: int):return n * 10**int(math.log10(m) + 1) + m
print(inserta(7, 654321))