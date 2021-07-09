'''
Si un amigo, no tan amigo, me presta K pesos a i pesos de interes
diario, ¿cuanto le pagaré en una semana si el interes es simple?, ¿y
cuanto si el interes es compuesto?.
'''

def interes_simple(k, i, t):
    return (k * i * t) + k

def interes_compuesto(k, i, t):
    return (k * (1 + i)**t) + k

k = float(input("¿Cuál es el monto prestado?: "))
i = float(input("¿Cuál es la tasa de interés?: "))
t = float(input("¿En cuanto tiempo se pagará?: "))

print("Escoja 1 si quiere hacer el cálculo para interés simple, o escoja 2 si quiere hacer el cálculo para interés compuesto")
a = int(input())

if a == 1:
    print("En el tiempo escogido, usted pagará", interes_simple(k,i,t), "de deuda")
elif a == 2:
    print("En el tiempo escogido, usted pagará", interes_compuesto(k,i,t), "de deuda")
else:
    print("No ha escogido una opción válida")
