ord("a")
print((bin(65)))
print(chr(65))
print(hex(65))
print(ord("A"))
print('"hola mundo"')
print('\'Hola\' mundo')
print("hola \\ mundo")
print("a"=="a")
print("a"=="A")
nombre = "Juan José"
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])
print(nombre[4])
print(nombre[5])
print(nombre[6])
print(nombre[7])
print(nombre[8])

if "Ju" in nombre:
    print("sí")
else:
    print("no")

if "Ha" in nombre:
    print("sí")
else:
    print("no")

for letra in nombre:
    print(letra, end=",")
z = 10
print(dir(nombre))
print(dir(z))

y = "hola\nmundo"
a = "hola\tmundo"
print(y)
print(a)

print(len(nombre))
print(nombre[len(nombre)-1])

b = "Minch Yoda XXX"
print(len(b), "caracteres")
for ejercicio in b:
    print(ejercicio)


'''
nombre="hfgh"
contador = 0
for espa in nombre:
    if espa == " ":
        contador = contador + 1         #Este ejemplo tiene errores



print (contador+1)
'''


print(nombre.count("Ju"))
print(nombre.find("Ju"))
print(nombre.lower())
print(nombre.upper())
print(nombre.capitalize())
print(nombre.title())
print(nombre.swapcase())
