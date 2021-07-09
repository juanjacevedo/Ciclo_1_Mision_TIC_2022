'''
Imprima los nombres completos (nombre y apellidos) de las personas
que practican el deporte ingresado por el usuario.
'''
from pprint import pprint
import json

data = {
"jadiazcoronado":{
"nombres": "Juan Antonio",
"apellidos": "Diaz Coronado",
"edad":19,
"colombiano":True,
"deportes":["Futbol","Ajedrez","Gimnasia"]
},

"dmlunasol":{
"nombres": "Dorotea Maritza",
"apellidos": "Luna Sol",
"edad":25,
"colombiano":False,
"deportes":["Baloncesto","Ajedrez","Gimnasia"]
}
}

with open("archivo.json", "w", encoding = "utf-8") as f:
    json.dump(data, f)

with open("archivo.json", "r", encoding = "utf-8") as f:
    data = json.load(f)
    deporte = input("Ingrese el deporte: ")
    print("el deporte es prácticado por: ")
    for value in data:
        if deporte in data[value]["deportes"]:
            cadena = data[value]["nombres"] + " " + data[value]["apellidos"]
            print("-", cadena)
#print(data["jadiazcoronado"]["nombres"], data["jadiazcoronado"]["apellidos"])
#pprint(data)
