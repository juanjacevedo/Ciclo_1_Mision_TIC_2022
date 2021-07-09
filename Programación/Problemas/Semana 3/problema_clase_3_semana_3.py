texto = str(input("Ingrese un texto o carácter sin espacio al final: "))
#Se pide que ingrese al usuario por pantalla. Este debe ser str porque en .count  se evaluará un string
texto_minuscula = texto.lower()
#Se transforma todo texto ingresado a minuscula porque algunas mayusculas tienen código binario parecido al de espacio ("100000")
binario = " ".join(format(ord(c), 'b') for c in texto_minuscula)
#La función .join convierte una lista en una cadena formada por los elementos de la lista separados por comas y la función integrada format() devuelve una representación formateada de un valor dato controlado por el especificador de formato.
espacio = int((binario.count("100000")))

if texto == "":
    print("No hay cadena de texto, palabras o caracteres")
    #Esta línea de código es para cuando el usuario no ingresa nada

elif espacio == 0:
    print("Hay una cadena de texto, palabra o carácter")
    #Si binario.count("100000") retorna 0, significa que no hay espacios en lo ingresado por el usuario y por tanto hay una cadena de texto, palabra o carácter

elif espacio == 1:
    print("Hay dos cadena de texto, palabras o caracteres")
    #Si binario.count("100000") retorna 1, significa que hay un sólo espacio entre lo que ingresó el usuario y por tanto hay dos cadena de texto, palabras o caracteres

else:
    print("Hay", espacio + 1,"cadena de texto, palabras o caracteres")
    #Si binario.count("100000") retorna un valor diferente a 0 y 1 (ya que este nunca tomará un valor negativo), quiere decir que en lo ingresado por el usuario hay más de un espacio y por tanto hay varias cadenas de texto, palabras o caracteres



#Corregir el código porque es susceptible a signos y a espacios en blanco
