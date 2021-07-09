import json

#import os
#os.mkdir("json")


data = {
    "cientifico": {"nombre": "Alan Turing", "edad": "41"}
}
print(type(data))

with open("json/data_file.json", "w") as write_file:
    json.dump(data, write_file) #seriealizando el obejto
    json_string = json.dumps(data, indent=4) #para volver el objeto data en un string con una identación que se realiza a 4 espacios
    print(json_string, type(json_string))

with open("json/data_file.json", "r") as read_file:

    data = json.load(read_file) #El método load es para cargar el objeto json a una variable
    print(type(data))
    print(data["cientifico"])



json_string = '''{"cientifico":
    {"nombre":"Alan Turing","edad":"41"}}'''
data = json.loads(json_string) #El método loads es para cargar el objeto json a una variable desde un json_string
print(data)


import json
from pprint import pprint
strjson = '''{"boolean1": null,"diccionario": {"papa": 2000, "arroz": 5000},
"intValue": 0, "myList": [],"myList2":["info1", "info2"],"littleboolean": false, "myEmptyList": null,
"text1": null, "text2": "hello", "value1": null,"value2": null}'''
data = json.loads(strjson)
pprint(data) #Para imprimir "bonito"


print(data["text2"], type(data["text2"]))
print(data["text1"], type(data["text1"]))
print(data["intValue"], type(data["intValue"]))
print(data["myList"], type(data["myList"]))
print(data["myList2"], type(data["myList2"]))
print(data["diccionario"], type(data["diccionario"]))
print(data["myList2"][1])
print(data["diccionario"]["papa"])


import json
import requests #Para realizar una petición
from pprint import pprint

response = requests.get("https://jsonplaceholder.typicode.com/todos") #Para leer un archivo JSON de una url especifica
pendientes = json.loads(response.text) #Para cargar el archivo JSON de la url especifica

pprint(pendientes) #Imprime el JSON cargado

