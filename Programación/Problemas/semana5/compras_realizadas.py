'''
Dado el archivo de texto files/Salesjan2009.csv, procese el archivo
para obtener las compras realizadas en un país dado.
'''
import csv
from pprint import pprint

dict = {}


with open("Ciclo 1\Programación\Problemas\semana5\SalesJan2009.csv", "r") as f:
    data = csv.reader(f,skipinitialspace = True) #El skipinitialspace es para quitar los espacios
    
    pais = input("Ingrese el país: ")
    dict[pais] = 0

    for linea in data:

        if linea[7] == pais:
            dict[pais] += 1
        # else:
        #     dict[linea[7]] = 1

pprint ("Está: " + str(dict[pais]) + " veces")



