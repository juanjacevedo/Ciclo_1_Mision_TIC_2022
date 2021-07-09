'''Dise ̃nar una funci ́on que permita calcular el  ́epsilon de la m ́aquina. El
 ́epsilon de m ́aquina es el n ́umero decimal m ́as peque ̃no que sumado
a 1 se puede representar de manera precisa en la m ́aquina (que no es
redondeado), es decir, retorna un valor diferente de 1,  ́este da una idea
de la precisi ́on o n ́umero de cifras reales que pueden ser almacenadas
en la m ́aquina. La idea es realizar un ciclo en el cual se realiza la
operaci ́on 1 + e para potencias de 2 desde e = 2^0 y continuando con potencias
decrecientes de 2 (e = 2^-1, e = 2^-2, e = 2^-3, e = 2^-4, . . . hasta obtener que
el resultado de la suma 1 + e no se altere.'''

def min_maquina():
    Xo = 1.0
    Xi = Xo / 2.0
    while Xi > 0.0:
        Xo = Xi
        Xi = Xo / 2.0
    return Xo
print("El mínimo número positivo", end = " ")
print("en esta máquina es:", min_maquina())

xo = 1
n = 0
e = 2
x = xo + e**n

while x > 1:
    x = xo + e**n
    n -= 1

print("El resultado de la suma 1 + e", end = " " )
print("sin que el valor de la suma se altere, es: ", xo, end = "")
print("+"+ str(e) + "^" + str(n) + " = " + str(x))
