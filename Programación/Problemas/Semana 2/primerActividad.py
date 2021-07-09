#Tarea de práctica de discurso de un político

#Librería
import random

#Definición de listas
lambetazo = ["Queridos", "Apreciados", "Distinguidos", "Honorables",
        "Estimados","Respetados"]
potenciales = ["compatriotas", "conciudadanos",
        "amigos", "coterraneos", "electores"]
condicion = ["en mi gobierno", "con su apoyo", "siendo elegido",
        "con suayuda", "si me siguen", "durante mi mandato"]
compromiso = ["voy a derrotar", "venceré", "eliminaré", "acabaré",
        "lucharé contra", "combatiré"]
ilusion = ["la violencia y", "la delincuencia y", "la corrupción y",
        "la inflación y", "la pobreza y", "el desplazamiento y"]
promesa = ["trabajaré por", "garantizaré", "protegeré", "velaré por",
        "promoveré", "defenderé"]
beneficio = ["la educación", "el empleo", "la seguridad", "la paz",
        "la igualda", "la salud"]

#Utilización de la librería
lambetazo_seleccionado = random.choice(lambetazo)
potenciales_seleccionado = random.choice(potenciales)
condicion_seleccionado = random.choice(condicion)
compromiso_seleccionado = random.choice(compromiso)
ilusion_seleccionado = random.choice(ilusion)
promesa_seleccionado = random.choice(promesa)
beneficio_seleccionado = random.choice(beneficio)

#Imprimimos resultado
print("Discurso: " + lambetazo_seleccionado + " " + potenciales_seleccionado +
        ", " + condicion_seleccionado + " " + compromiso_seleccionado + " " +
        ilusion_seleccionado + " " + promesa_seleccionado + " "
        + beneficio_seleccionado)
