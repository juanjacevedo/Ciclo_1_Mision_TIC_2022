tupla = 1, 2, 3, 'A', (10, 20, ('a', 'b'), 30), [20, 30, 40]
print(tupla)
print(type(tupla))

#tupla.append(1000)
lista = list(tupla) #Convertir una tupla en lista
lista.append(1000) #Le agregó otro dato a la lista
#lista.remove(1000) #Le quito un dato a la lista
print(lista)
print(type(lista))

tupla2 = tuple(lista) #Convertir la lista en tupla
print(tupla2)
print(type(tupla2))
print(dir(tupla2))

#-------------------------------------------------------------------------------

mi_tupla = ('1',) #La coma marca la diferencia entre tuple y string
print(mi_tupla)
print(type(mi_tupla))
print(tupla[-1][1]) #Para acceder al segundo elemento del ultimo elemento de la tupla


tupla3 = tupla + mi_tupla #Concatenación de tuplas
print(tupla3)
print(type(tupla3))

tuplaA = 'enero', 'febrero' * 2
tuplaB = 'marzo', 'abril'
# Las tuplas también se pueden multiplicar
tuplaC = tuplaA + tuplaB*2
print(tuplaC)

'''a = input("")
tuple(a)
print(tuple(a))'''

#-------------------------------------------------------------------------------

print(('Rojas',123) < ('Rosas',123))

print(('Rosas',123) == ('rosas',123))

print(('Rosas',123) > ('Rosas',123))

print(('Rojas',"123") > ('Rosas',23))

#print(('Rosas',"123") > ('Rosas',23))

text = 'cien', 'anios', 'de', 'soledad'

if 'anios*' in text:
    print('Sí está en la tupla')
else:
    print('No está en la tupla')


for x in text:
    if x == 'anios*':
        print('Sí está en la tupla')
        break
else:
    print('No está en la tupla')

tuple1 = 1, 2, 3, (1,2)

a = 1
b = 3

a, b = b, a

print('a =', a)
print('b =', b)

tuple2 = 1,2,3,4,5

a,b,c,d,e = tuple2

print(a,b,c,d,e)

tuple3 = (11,9,-2,3,8,5)

var1, var2, var3, var4 = (tuple3[1] for i in (1,3,5,1))

print("var1 = ", var1, ", var2 = ", var2, ",var3 = ", var3, ",var4 =", var4)
