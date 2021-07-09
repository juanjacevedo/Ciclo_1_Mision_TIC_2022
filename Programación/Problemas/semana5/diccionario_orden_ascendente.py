'''
Desarrollar un algoritmo que imprima de manera ascendente los
valores (todos del mismo tipo) de un diccionario.
'''
from pprint import pprint
import operator

dic1 = { "clave4":"4621",
        "clave1":"6425",
        "clave3":"1234",
        "clave2":"2354"
        }

dic2 = { "4621":"Juan",
        "6425":"Pedro",
        "1234":"Alberto",
        "2354":"Andrea"
        }

dic3 = { "nombre":["Juan", "Pedro", "Alberto", "Andrea"],
        "apellido":["Acevedo","Otalora", "Gimenez", "Castro"],
        "id":["4621","6425","1234","2354"],
        "ciudad": ["Medellín","Bogotá","Cali","Manizales"]
        }


#Ordenado por clave

def orderByKey(diccionario):
        diccionario = sorted(diccionario)
        return diccionario

print(orderByKey(dic1))
print(orderByKey(dic2))
print(orderByKey(dic3))

#Ordenar devolviendo una lista que incluye clave y valor

def orderByKeyAndValue(diccionario):
        diccionario = sorted(diccionario.items())
        return diccionario

pprint(orderByKeyAndValue(dic1))
pprint(orderByKeyAndValue(dic2))
pprint(orderByKeyAndValue(dic3))


#Ordenar por clave

def orderByValue(diccionario):
        diccionario = sorted(diccionario.items(), key = operator.itemgetter(1), reverse=False)
        return diccionario
pprint(orderByValue(dic1))
pprint(orderByValue(dic2))
pprint(orderByValue(dic3))