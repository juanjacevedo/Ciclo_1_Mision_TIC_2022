'''
Dadas tres longitudes positivas, determinar si con esas longitudes se
puede construir un triangulo.
'''

def triangulo(a,b,c):
    if a >= b + c:
        return str("Con estas longitudes no se puede construir un triángulo")
    elif b >= a + c:
        return str("Con estas longitudes no se puede construir un triángulo")
    elif c >= b + a:
        return str("Con estas longitudes no se puede construir un triángulo")
    else:
        return str("Con estas longitudes sí es posible construir un triángulo")

a = float(input("Valor de la primer longitud: "))
b = float(input("Valor de la segunda longitud: "))
c = float(input("Valor de la tercera longitud: "))

print(triangulo(a,b,c))
