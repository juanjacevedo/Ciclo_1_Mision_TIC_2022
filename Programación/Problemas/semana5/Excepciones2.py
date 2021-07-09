'''
Capture la excepcion para evitar que un programador sume una
cadena de texto a un numero y muestre el mensaje
Los tipos de datos no cuadran para hacer la operacion:

def operar(a, b):
    return a+b
def main():
    a = int(input())
    b = ’hola’
    operar(a, b)
main()
'''

try: 
    def operar(a, b):
        return a+b
    def main():
        a = int(input())
        b = "hola"
        operar(a, b)
    main()
except:
    print("Los tipos de datos no cuadran para hacer la operacion")