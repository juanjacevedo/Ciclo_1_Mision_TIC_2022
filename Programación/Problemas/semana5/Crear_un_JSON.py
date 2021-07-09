'''
Cree un JSON de deportes como sigue:
'''


import json

data = {
"Ajedrez":["jadiazcoronado","...","dmlunasol"],
"Futbol":["jadiazcoronado","..."],
"Gimnasia":["jadiazcoronado","...","dmlunasol"],
"..."
"Baloncesto":["...","dmlunasol"]
}

with open("deportes.json", "w", encoding="utf-8") as a:
    json.dump(data, a)