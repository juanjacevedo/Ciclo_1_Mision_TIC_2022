y = 5
x = 2
print(y//x)#División de parte entera
print(y**x)#Potencia
print(y%x)#Modulo

a = 4
b = 3

a += b #Asignación aumentada "Otra manera de sumar,restar, dividir..."
print(a)
b -= a
print(b)

a = 4
b = 3
a %= b
print(a)
b /= a
print (b)

v = True
f = False

print (not v) #Operadores lógicos
print (v and (v == f))
print (v or (v == f))

x = 5
y = 10

print (y == x + x)
print (y != x + x)
print (y <= x)
print (y >= x)
print (y < x)
print (y > x)
print (y > x or y < x)
print (y > x and y < x)

#Gerarquía de Operadores
# 1. ()
# 2. not, -, +, **
# 3. +, /, //, %
# 4. +, -
# 5. <, >, >=, <=
# 6. ==, !=
# 7. and
# 8. or
# 9. =, +=, -=, *=, /=, //=, %=

def potencia_de_un_numero(numero, potencia): #función
    valor = numero**potencia
    return valor

print(potencia_de_un_numero(5,3))


def areaCirculo(radio):
    A = 3.14159265359 * (radio**2)
    return A

print(areaCirculo(3))
