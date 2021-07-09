'''
Modele mediante una funci ́on matem ́atica y dise ̃ne un programa
recursivo sin cadenas, tuplas o listas que dado un n ́umero natural n
elimine el  ́ultimo d ́ıgito del n ́umero. Por ejemplo,
elimina_ult(654321) = 65432.
'''
'''
def elimina_ult(n):
    if n < 0: return str("Igrese un número natural")
    elif n == 0: return n
    else:
        n = str(n)
        return n[:-1]
print(elimina_ult(654321))
'''

def elimina_ult(n):
    if n < 0: return str("Igrese un número natural")
    elif n == 0: return n
    else: return n // 10
print(elimina_ult(654321))