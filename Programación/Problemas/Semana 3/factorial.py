'''Imprimir los numeros de 1 hasta un numero natural n dado, cada uno
con su respectivo factorial.'''

x = 2
n = 1
m = int(input("Ingrese el número hasta el que se desea imprimir: "))
print("Número", end = " ")
print("-> Factorial")

for secuencia in range(1, m + 1, 1):

    x = n * (x - 1)
    print(secuencia, end = " ")
    print("->",x)
    n += 1
    x += 1
