'''suma = 0
dato = -1
while(dato != 0):
    dato = int(input("ingrese un número entero" + " a sumar o 0 para salir: "))
    suma += dato
print("La suma es: " + str(suma))
'''


'''frutas = ["Tomate de árbol", "Maracuyá", "Guayaba"]

for f in frutas:
    print(f)
else:
    print("No hay más frutas")
'''

'''frutas = ["Tomate de árbol", "Maracuyá", "Guayaba"]

for f in frutas:
    print(f)
    if(f == "Maracuyá"):
        break
'''

'''frutas = ["Tomate de árbol", "Maracuyá", "Guayaba"]

existe = True

for f in frutas:
    print(f)
    if(f == "Maracuyá"):       Revisar bien cómo hacer esta con booleanos
        #existe = False
        break
    else:
        pass
'''

'''print(sum(range(5)))'''

'''for secuencia in range(10, -1, -1):
    print(secuencia)
else:
    print("¡Feliz año!")
'''

for secuencia in range(10, 0, -1):
    if secuencia % 2 == 0:
        print(secuencia, " es par")
    else:
        print(secuencia, " es impar")
else:
    print("¡Feliz año!")
