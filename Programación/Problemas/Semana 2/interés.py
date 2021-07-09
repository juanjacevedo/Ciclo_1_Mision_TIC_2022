'''
Si pido prestados P cantidad de pesos para pagarlos en dos meses, si
el interés del préstamo es del 3% al mes. ¿Cuánto se debe pagar al
final del segundo mes si el interés es compuesto mensualmente?.
'''

def interes_compuesto(p, i, t):
    return (p * (1 + i)**t) + p

p = float(input("Monto del prestamo: "))
print("Usted debe pagar",interes_compuesto(p,0.03,2),"pesos")
