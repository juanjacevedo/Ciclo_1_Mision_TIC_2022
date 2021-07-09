'''
Modele mediante una funci ́on matem ́atica y dise ̃ne un programa
recursivo sin cadenas, tuplas o listas que dado un n ́umero natural n
elimine el primer d ́ıgito del n ́umero. Por ejemplo,
elimina pri(654321) = 54321.
'''
import  math
def elimina_pri(n:int): return n % 10**int(math.log10(n))
print(elimina_pri(654321))