'''
def lee_arreglo_enteros():
    return[int(x) for x in input("Arreglo:").split()]

print(lee_arreglo_enteros())

def lee_arreglo_enteros2():
    return[float(x) for x in input("Arreglo:").split(",")]

print(lee_arreglo_enteros2())

def suma_arreglo(A):
    s = 0
    for x in A:
        s += x
    return s

print(suma_arreglo([1,-3,4,11,6]))

def pos_maximo(A):
    m=0
    for i in range(1,len(A)):
        if A[i] > A[m]:
            m = i
    return m
print(pos_maximo([1,-3,4,11,6]))


m = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

for i in m:
    for j in i:
        print(j,end=" ")
    print()


def cuadrados_matriz(x):
    y = []
    for i in range(len(x)):
        fila = []
        for j in range(len(x[i])):
            fila.append(x[i][j]*x[i][j])
        y.append(fila)
    return y

print(cuadrados_matriz([[1,-3,2],[4,11,-1]]))
'''

def cuadrados_matriz(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = input("Ingrese valor: ")
    return x

c = int(input())
f = int(input())

m = [([None]*c) for x in range(f) ]

print(cuadrados_matriz(m))
