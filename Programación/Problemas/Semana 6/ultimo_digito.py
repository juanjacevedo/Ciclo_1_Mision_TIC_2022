'''
Modele mediante una funci ́on matem ́atica y dise ̃ne un programa sin
cadenas, tuplas o listas que retorne el  ́ultimo d ́ıgito de un n ́umero
natural n (le ́ıdo de izquierda a derecha). Por ejemplo,
ultimo(13579) = 9.
'''


def ultimo(n):
    if n < 0: return str("Igrese un número natural")
    else: return n % 10

print(ultimo(13579))

'''
def numero(n):
    if n < 0: return str("Igrese un número natural")
    else:
        n = str(n)
        return n[-1]

def ultimo(n):
    print(numero(n))

ultimo(13579)
'''