'''
Dados dos numeros reales distintos de cero (0), x y y que representen
la abscisa y ordenada de un punto (x; y) pertenciente a R², determinar a que
cuadrante del plano cartesiano pertenece el par ordenado.
'''

def cuadrante(x,y):
    if x > 0 and y > 0:
        return str("Las coordenadas pertenecen al primer cuadrante")
    if x < 0 and y > 0:
        return str("Las coordenadas pertenecen al segundo cuadrante")
    if x < 0 and y < 0:
        return str("Las coordenadas pertenecen al tercer cuandrante")
    if x > 0 and y < 0:
        return str("Las coordenadas pertenecen al cuarto cuadrante")

x = float(input("Ingrese el valor del abscisa: "))
y = float(input("Ingrese el valor de la ordenada: "))
print(cuadrante(x,y))
