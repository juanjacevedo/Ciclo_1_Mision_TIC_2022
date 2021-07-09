'''
El siguiente c ́odigo abre el archivo y muestra su contenido:
'''

with open("files/data.txt", "r") as f:
    data = f.read()
    print(data)


'''
El comando open(ruta del archivo, ’w’) abre esl archivo en modo de
escritura creando el archivo si no existe (write)  ́o sobreescribiendo el
archivo si existe.
'''

with open("files/wdata.txt", "w") as f:
    data = "estamos escribiendo en el archivo 123\n"
    f.write(data)
    f.write(data)
    f.write(data)

'''
El comando open(ruta del archivo, ’a’) abre el archivo en modo de
adjuntar creando el archivo si no existe (append )  ́o escribiendo al final del
archivo si existe.
'''

with open("files/wdata.txt", "a") as f:
    data = "más cosas\n"
    f.write(data)
    f.write(data)
    f.write(data)
'''
Para el archivo data1.txt ubicado en la carpeta files
'''
with open("files/data1.txt", "r") as f:
    print(f.read())

'''
En caso de tener problemas de codificaci ́on se puede agregar el par ́ametro
encoding="utf-8" al comando with open.
'''

with open("files/data1.txt", "r", encoding="utf-8") as f:
    print(f.read())

'''
El siguiente c ́odigo lo abre, lee su contenido completo y lo imprime:
'''
with open("files/data1.txt", "r", encoding="utf-8") as f:
    print(f.read())

'''
En algunos casos no se desea leer la totalidad del contenido de un archivo,
sino solamente una fracci ́on, en ese caso el comando read() admite un
par ́ametro entero que especifica cuantos bytes se leen y deja el apuntador
justo despu ́es del  ́ultimo byte le ́ıdo.

Si se desea leer en primera instancia los primeros 6 bytes y a continuacion
los siguientes 10 bytes, se puede utilizar la instruccion:
'''

with open("files/data1.txt", "r", encoding="utf-8") as f:
    linea1 = f.read(6)
    linea2 = f.read(10)
    #linea = f.read()

print(linea1)
print(linea2)
#print(linea)

'''
Es posible leer un archivo linea por l ́ınea utilizando el comando
readline(). Esta es una forma eficiente en memoria de leer un archivo:
Para el archivo data1.txt ubicado en la carpeta files

El siguiente c ́odigo abre el archivo, lee el contenido de las dos primeras
l ́ıneas y las imprime con un s ́olo salto de l ́ınea entre ellas:
'''

with open("files/data1.txt", "r", encoding="utf-8") as f:
    linea1 = f.readline()
    linea2 = f.readline()

print(linea1, end="")
print(linea2, end="")

'''
El siguiente c ́odigo abre el archivo, lee el contenido completo del archivo y
lo almacena en una lista l ́ınea por l ́ınea:
'''

with open("files/data1.txt", "r", encoding="utf-8") as f:
    print("Nombre del archivo: ", f.name)
    lista = f.readlines()

print(lista)

'''
El siguiente c ́odigo permite procesar eficientemente el contenido del
archivo
'''

with open("files/data1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")

'''
El siguiente c ́odigo permite a ̃nadir una nueva l ́ınea al final del archivo
'''

with open("files/data2.txt", "a+", encoding="utf-8") as f:
    f.write("\nEsta es la linea 4: abcabcabc")

'''
El siguiente c ́odigo permite escribir en el archivo data3.txt una serie de
datos almacenados en una lista luego de convertirse cada uno a cadena.
'''

values = [1234, 5678, 9012, 3.14159265, False]
with open("files/data3.txt", "w+") as f:
    for value in values:
        str_value = str(value)
        f.write(str_value)
        f.write("\n")


'''
El siguiente c ́odigo permite ubicar el puntero en la posici ́on 11 dentro del
archivo
'''

with open("files/data4.txt", "r", encoding="utf-8") as f:
    f.seek(11,0)
    for line in f:
        print(line, end="")

'''
Para determinar el tama ̃no del archivo data4.txt en bytes se puede
utilizar la instrucci ́on
'''
with open("files/data4.txt", "a+") as f:
    print(f.tell())

'''
El siguiente c ́odigo abre el archivo data5.txt en modo lectura, lee su lista
de lineas, inserta una nueva l ́ınea en la lista, lo abre de nuevo data5.txt
en modo escritura y escribe en  ́este la totalidad del contenido de la lista.
# Abre el archivo en modo de s ́olo lectura
'''
with open("files/data5.txt", "r", encoding="utf-8") as f:
    list_content = f.readlines()

list_content.insert(1, "Esta es la l ́ınea 1.5: jajaja\n")

# Re-abre el archivo en modo de s ́olo escritura
# para sobreescribir la versi ́on anterior de  ́este
with open("files/data5.txt", "w", encoding="utf-8") as f:
    contenido = "".join(list_content)
    f.write(contenido)

'''
Para el directorio files, el siguiente c ́odigo permite caracterizar el
contenido de archivos y subdirectorios contenidos en  ́este.
'''

import os
entries = os.scandir("files/")
for entry in entries:
    print(entry.name + ", es directorio: "
    + str(entry.is_dir()) + ", size: " +
    str(entry.stat().st_size) + " bytes.")


'''
El siguiente c ́odigo permite crear dos lista, un diccionario a partir de  ́estas
y por  ́ultimo se serializan como objetos
'''

import pickle
name = ["mohit", "bhaskar", "manish"]
skill = ["Python", "Python", "Java"]
dict1 = dict([(k,v) for k,v in zip(name, skill)])
with open("files/programming_powers.pkl", "wb") as p_file:
    pickle.dump(name, p_file)
    pickle.dump(skill, p_file)
    pickle.dump(dict1, p_file)

'''
Para realizar el proceso inverso de serializaci ́on (leer de archivo los objetos
serializados con pickle), se puede seguir el m ́etodo load:
'''

import pickle

with open("files/programming_powers.pkl", "rb") as p_file:
    list1 = pickle.load(p_file)
    list2 = pickle.load(p_file)
    dict1 = pickle.load(p_file)
print(list1)
print(list2)
print(dict1)