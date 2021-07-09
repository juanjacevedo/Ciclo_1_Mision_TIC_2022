'''Dise~ne un programa que muestre las tablas de multiplicar del 1 al 9.'''

for i in range(0, 10, 1):
    print()
    for j in range(0, 11, 1):
        print(i, "x", j, "=", i * j)
