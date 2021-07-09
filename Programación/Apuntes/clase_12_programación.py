str2 = """It is not despair, for despair is
only for those who see the end
beyond all doubt. we do not."""

print(str2)
print("first:", str2.find("despair"))
print("last:", str2.rfind("despair"))
#-------------------------------------------------------------------------------

str3 = "  Hola mundo  "
print(str3)
str4 = str3.strip()
print(str4)

print(str3.lstrip("  Ho"))

str5 = "01-06-2021"

arraytmp= str5.split("-")
print(arraytmp)
print(arraytmp[2])
print(str5.split("-"))

i = "Ganador del premio por responsabilidad social"
arreglo_i = i.split(" ") # --> Esto soluciona el reto de la clase anterior
print(arreglo_i, "AAAAAAAAAA")
print(len(arreglo_i))

#-------------------------------------------------------------------------------

str = "Hola mundo"
print(str.replace("mu", "+"))
print(str.ljust(15,"#"))
print(str.rjust(15, "#"))
print(str.center(15, "#"))
account = "123456789"
print(account.zfill(15), "account")
print(str.endswith("o"))
print(str.endswith("d"))
print(str.startswith("o"))
print(str.startswith("H"))
print(str.isdigit())
print(str.isalnum())
print(str.islower())        #La explicación de estas funciones está en las diapositivas de la semana 3
print(str.isupper())
print(str.isspace())
print(str.isalpha())

ejemplo = input("Ingrese cualquier texto: ")
print(ejemplo[-1] + ejemplo[1:len(ejemplo)-1] + ejemplo[0])

"""
def cambio(cadenita):

    str1 = cadenita[len(cadenita)-1] + cadenita[1:len(cadenita)-1] + cadenita[0]
    return str1


cadenita = str(input("Typer your word:"))
print(cambio(cadenita))
"""
