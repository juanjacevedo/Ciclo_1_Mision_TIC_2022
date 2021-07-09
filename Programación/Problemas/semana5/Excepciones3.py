'''
Capture la excepcion cuando se trata de obtener una llave que no se
encuentra en un diccionario y muestre el mensaje
Intenta acceder una llave que no esta en el diccionario:
def main():
    dict = {’James’: ’Java’, ’Dennis’ : ’C’, ’Das’:’Python’}
    print(dict[’Ada’])
main()
'''
def main():
    try:
        dict = {'James': 'Java', 'Dennis' : 'C', 'Das':'Python'}
        print(dict["Ada"])
    except:
        print("Intenta acceder una llave que no esta en el diccionario")

main()
    