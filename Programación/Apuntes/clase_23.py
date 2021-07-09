'''
def log_entero(num, base=2):
    cont = 0
    while num >= base:       
        cont +=1
        num /=base
    return cont


def variable_argument(var1, *vari): # arguments
    print("salida:" + str(var1))

    print(type(vari))
    for var in vari:
        print(var)

variable_argument(100,90,67,23,10)

from pprint import pprint

def informar(**var): #kwarguments
    pprint(var)
    
    for key, value in var.items():
        pprint("%s == %s vecessss" % (key, value))

informar(nombre="poseidon", edad=6000, ciudad = "olimpo")

def unir_listas(lista1, lista2):
    lista1.extend(lista2)

avengers = ["Tony", "Natalia", "Steve"]
nuevos_avengers = ["Thor", "Peter"]

unir_listas(avengers, nuevos_avengers)
print(avengers)

def func(a):
    a *= 10
    print('En la funci ́on a =',a)

a = 45
func(a)
print('En el programa principal a =',a)

def no_limpia_lista(lista):
    lista = []

avengers = ["Tony", "Natalia", "Steve"]
no_limpia_lista(avengers)
print(avengers)

def func():
    a=12
    print("Variable local:", a)

a = 10
func()
print ("Variable del cuerpo principal:",a)


k = 4 #Variable global
def main():
    lista = []
    def add():
        for x in range(k):
            lista.append(x)
        print(lista)
    add()
main()

k=5
def func():
    global k
    k=k+7
    print("La variable k tiene alcance global:",k)
    k=10

func()
print ("Valor de la variable global k fuera de la función:",k)

x = "sorprendente"

def myfunc():
    global x
    x = "fant ́astico"

print("Antes Python era " + x)
myfunc()
print("Ahora Python es " + x)
'''

import modulo as m # "m" es sólo una etiqueta
x = 12
y = 34
print ("La suma es ", m.sum1(x,y))
print ("La multiplicación es ", m.mul1(x,y))


from modulo import sum1
x = 12
y = 34

print("La suma es ", sum1(x,y))

'''
Cuando se utiliza import, python buscará el módulo en la siguiente forma:
-El directorio actual
-La variable de entorno PYTHONPATH
Para ver informaci ́on sobre las rutas usadas por Python para import:
'''

import sys
for p in sys.path:
    print(p)

from comprimir import aZip
from comprimir import aRar
from comprimir import aTar
aZip.crear_zip("archivo")
aRar.crear_rar("archivo")
aTar.crear_tar("archivo")

'''
import sys

sys.path.append("/ruta/module1")
sys.path.append("/ruta/module2")

from lib.module1 import A
from lib.module2 import B
'''
