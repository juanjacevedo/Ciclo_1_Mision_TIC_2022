'''
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen
N gallinas, M gallos y K pollitos. Cada uno pesando 6 kilos, 7 kilos  y 1 kilo
respectivamente.
'''
def kilos_carne(N, M, K):
    kilos = 6*N + 7*M + 1*K
    return kilos
print("La cantidad de carne de aves en kilos, es: ", kilos_carne(float(input("Ingrese el número de gallinas: ")),float(input("Ingrese el número de gallos: ")),float(input("Ingrese el número de pollitos: "))))
