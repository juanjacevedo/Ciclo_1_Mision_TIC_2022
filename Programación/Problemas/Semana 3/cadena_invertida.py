'''Desarrollar un algoritmo que invierta una cadena de caracteres.'''
a = input("Ingrese un texto: ")
arreglo_a = a.split()
arreglo_b = arreglo_a[::-1]
print("El texto invertido es: " + " ".join(arreglo_b))
