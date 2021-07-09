'''
Si en la UN estan podando  ́arboles y cada rama tiene P hojas, y a
cada  ́arbol le quitaron K ramas, cuantos  ́arboles se deben podar para
obtener T hojas?.
'''

def arboles(P, K, T):
    return T / (P * K)
    #Siendo (P * K) el número de hojas por árbol
    #Siendo T / (P * K) el número de árboles a podar

P = float(input("Número de hojas por rama: "))
K = float(input("Número de ramas por árbol: "))
T = float(input("Número de hojas que desea obtener: "))

print("El número de árboles que de deben podar para tener", T, "hojas, es: ", arboles(P,K,T))
