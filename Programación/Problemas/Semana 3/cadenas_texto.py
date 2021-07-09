'''Desarrollar un algoritmo que reciba dos cadenas de caracteres y
determine si la primera esta incluida en la segunda. Se dice que una
cadena esta incluida en otra, si todos los caracteres (con repeticiones)
de la cadena esta en la segunda cadena sin tener en cuenta el orden
de los caracteres.'''

palabra_1 = input("ingrese una palabra para saber si está en otra: ")
palabra_2 = input("ingrese la frase dónde se va a buscar:")
bandera = True
if len(palabra_1) > len(palabra_2):
    print("La palabra a buscar es mas grande que la otra por ende no está incluida")
else:
    for i in palabra_1:
        if palabra_1.count(i) > palabra_2.count(i):
            bandera = False
            break
        elif i not in palabra_2:
            bandera = False
    if bandera==True:
        print("la cadena \"" + palabra_1 + "\" está incluida en la cadena \"" + palabra_2 + "\"")
    else:
        print("la cadena \"" + palabra_1 + "\" no está incluida en la cadena \"" + palabra_2 +"\"")
