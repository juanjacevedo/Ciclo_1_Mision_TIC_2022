def año_nuevo(contador=5):
    for x in range(contador, -1, -1):
        print(x)
    else:
        print("¡Feliz año!")


año_nuevo(9)
año_nuevo()

def contar_año_recursiva(contador=5):
    if contador < 0: #Caso base
        print("¡Feliz año!") 
    else: #Caso recursivo
        print(contador)
        contar_año_recursiva(contador-1)


contar_año_recursiva()
contar_año_recursiva(12)

'''
calcular la suma de los números desde el 0 hasta n
'''
def sumar(n):
    if n > 0:
        return n + sumar(n-1)
    else:
        return 0

print(sumar(100)) #Guiño a Gauss 

'''
Calcular la suma de los números almacenados en una lista
'''
def sumar_parcial(L,n):
    if n > 0:
        return L[n-1] + sumar_parcial(L,n-1)
    else:
        return 0

def sumar_lista(L):
    return sumar_parcial(L,len(L))

lista = []
for v in range(1,5):
    lista.append(v)
print(lista)

print(sumar_lista(lista))

''' 
Realizar un juego que pregunte de qué color es el planeta marte. Si el usuario ingrese rojo, devolver un mensaje ganaste (perdiste en otro caso). El usuario tiene tres intentos
'''
def color_marte(n=3):
    entrada=input("Ingrese color: ")

    if entrada.lower() =="Rojo".lower():
        print("¡Ganaste!")
    elif n == 1:
        print("Perdiste")
    else:
        color_marte(n-1)

color_marte() 

