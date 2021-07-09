'''
El número de contagiados de Covid-19 en el país de NuncaLandia se
duplica cada día. Hacer un programa que diga el número total de
personas que se han contagiado cuando pasen D días a partir de hoy,
si el número de contagiados actuales es C.
'''

def contagiados(D, C):

    if D == 0:
        return C
    elif D < 0:
        return str("Error")
    elif C < 0:
        return str("Error")
    else:
        n = 1
        total = 1
        while n <= D:
            total = total + 2**n
            n += 1
            suma_total_contagiados = total * C
        return suma_total_contagiados

D = int(input("Días de contagio: "))
C = int(input("Número actual de contagiados: "))
print("El número total de contagiados es:", contagiados(D,C), "personas")
