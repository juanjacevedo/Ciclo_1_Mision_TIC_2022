estudiante = {"nombre" : "Juan", "apellido" : "Pérez", "edad": 30, "cursos" : ["P","I","C"]}

d = dict()
print (estudiante)
print(type(d))
estudiante["cédula"] = 1035441293
d = {"ciudad":"Medellín"}
estudiante.update(d)

print(estudiante)
print(estudiante["nombre"])
print(estudiante.get("nombre"))
print(estudiante.get("Nombre", "No existe"))

#del estudiante
#print(estudiante)

del estudiante["cursos"]
print(estudiante)

e = estudiante.pop("edad")
print(estudiante)
print(e)
