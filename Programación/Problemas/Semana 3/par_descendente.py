'''Imprimir los numeros pares en forma descendente hasta 2 que son
menores o iguales a un numero natural n <= 2 dado.'''

def parDescen(n):
    if n % 2 == 0:
        while n >= 2:
            if n == 2:
                return n
                n -= 2
            else:
                print(n)
                n -= 2
    else:
        print("Hola")

print(parDescen(-8))
