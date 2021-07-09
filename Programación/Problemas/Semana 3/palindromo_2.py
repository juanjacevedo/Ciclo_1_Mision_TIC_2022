''''
Desarrollar un algoritmo que determina si una cadena de caracteres es
frase palndrome, esto es, si es palndrome al eliminarle espacios,
tldes, signos de puntuacion y al considerar mayusculas=minusculas.
'''
#salida = ""
palabra = input("ingrese una cadena: ")
palabra = palabra.lower().replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace(",","").replace(";","").replace(".","")
palabra_2 = palabra[::-1]

if palabra_2 == palabra:
    print("Es palindromo")
else:
    print("No es palindromo")















"""
for i in palabra:



    salida = i + salida

if salida.lower() == palabra.lower():
    print("Es palindromo")

else: print("No es palindromo")
"""
