'''
Dado el centro y el radio de un crculo, determinar si un punto de R2
pertenece o no al interior del crculo.
'''

def pertenencia_circunferencia(xp,yp,xc,yc,r):
    d = ((xp-xc)**2 + (yp-yc)**2)**1/2
    if d <= r:
        return str("El punto está dentro del circulo")
    else:
        return str("El punto está fuera del circulo")

xp = float(input("Valor de la abcisa del punto: "))
yp = float(input("Valor de la ordenada del punto: "))
xc = float(input("Valor de la abcisa de la circunferencia: "))
yc = float(input("Valor de la ordenada de la circunferencia: "))
r = float(input("Valor del radio de la circunferencia: "))

print(pertenencia_circunferencia(xp,yp,xc,yc,r))
