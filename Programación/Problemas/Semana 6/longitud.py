'''
Modele mediante una funci ́on matem ́atica y dise ̃ne un programa
recursivo sin cadenas, tuplas o listas que determine la cantidad de
d ́ıgitos que componen un n ́umero natural n. Por ejemplo,
longitud(1230321) = 7.
'''
import math
def longitud(n:int): return int(math.log10(n))+1
print(longitud(1230321))