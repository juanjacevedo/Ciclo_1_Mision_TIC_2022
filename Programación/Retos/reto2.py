'''
En un concurso nacional de programación virtual, registraron a los concursantes
del evento en salas independientes y cada una de ellas está identificada al azar
con una letra única del alfabeto.

Dos de los administradores de la plataforma encargados en coordinar el acceso a
las salas, iniciaron una apuesta entre ellos para determinar el orden en el que
los asistentes ingresan a cada una de ellas. Los administradores acordaron, que
del total de salas disponibles se le asignara anticipadamente solo una parte a
cada uno, y a me dida que vayan llegando los asistentes se les acumula un bono
regalo según corresponda.

Por ejemplo, en el orden de llegada de ingreso de cada asistente, primero se
verifica a que sala pertenece y seguidamente se compara su cantidad y se asignan
los bonos. Así, si la sala corresponde al primer administrador y éste toma
ventaja, se le asigna un bono “A”, si por el contrario después de ingresar
el asistente la ventaja pertenece al segundo administrador, se le asigna un
bono “B”. En el caso que al ingresar un asistente y realizar el computo no
exista ventaja/desventaja para ninguno (misma cantidad de bonos) se asigna un
bono neutro “N”. Pada cada asistencia que no pertenezca a ninguno, se deberá
tener en cuenta el nombre del bono más reciente en el registro de bonos. Si la
sala en cuestión se encuentra asignada a ambos (o a ninguno), se considera
empate y no se tendrá incremento para ninguno de los dos.

Para ayudar en este juego, se requiere un programa que indique la secuencia de
los bonos obtenidos. Para ello, el programa deberá capturar la cadena de texto
que represente las letras de las salas asignadas a cada administrador, así como
la secuencia de los nombres de las salas en las que registraron el ingreso de
los asistentes a la plataforma.

Entrada

En la primera entrada, una cadena de texto que represente los nombres de las
salas asignadas al primer administrador. En la segunda entrada las salas
asignadas al segundo administrador, en la tercera entrada, el registro ordenado
con los nombres de las salas en las que asistieron los concursantes.

Salida

Una línea con la secuencia de nombres de bonos según el orden de asistencia
registrado.
'''
j = 1
a = 0
b = 0
admin1 = input()
admin2 = input()
salas = input()
lista = []

for i in salas[0]:
    if i in admin1:
        lista.append("A")
        a = a + 1
    elif i in admin2:
        lista.append("B")
        b = b + 1
    else:
        lista.append("N")

for i in salas[1:len(salas)]:
    if i in admin1:
        a = a + 1
        if a > b:
            lista.append("A")
        elif a < b:
            lista.append("B")
        else:
            lista.append("N")
    elif i in admin2:
        b = b + 1
        if a > b:
            lista.append("A")
        elif a < b:
            lista.append("B")
        else:
            lista.append("N")
    else:
        lista.append(lista[j-1])
    j = j + 1

print(len(salas))
print()
print(lista)
print(len(lista))
print("".join(lista))
