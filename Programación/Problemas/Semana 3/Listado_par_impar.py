'''Imprimir un listado con los numeros impares desde 1 hasta 999 y
seguidamente otro listado con los numeros pares desde 2 hasta 1000.'''
n = 1
while n <= 500 :
    par = 2*n
    print(par)
    n += 1

n -= n 
while n < 500 :
    impar = 2*n + 1
    print(impar)
    n += 1
