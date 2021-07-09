'''
def division(a, b):
    coc = a//b
    res = a % b
    return(coc, res)
                            #TODO: Este solo es un ejemplo
division(4,5)
print(division(10, 0))
print(division(1024, 10))


def division(a, b):
    try:
        coc = a // b
        res = a % b
        return(coc, res)
    except:
        print("Error en la división de", a, "entre", b)
        return ""

print(division(10, 0))
print(division(1024, 10))

def division(a, b):
    try:
        coc = a//b
        res = a % b
        return(coc, res)
    except:
        print("Error en la divisi ́on de", a, "entre", b)

def main():
    try:
        num = int(input("digite el dividendo: "))
        div = int(input("digite el divisor: "))
        print(division(num, div))
    except ValueError:
        print("El valor digitado no es un n ́umero.")
main()


try:
    num = int(input("Ingrese un n ́umero "))
    re = 100/num
except:
    print("Algo est ́a mal")
else:
    print("El resultado es ",re)
finally:
    print("El programa termina!")

try:
    num = int(input("Ingrese un n ́umero: "))
    re = 100/num # Generar excepci ́on si se digit ́o 0
    print(re)
except Exception as e:
    print(e, "\n", type(e))

def division(a, b):
    if b == 0:
        raise ValueError("!Error de divisi ́on por cero¡")
    else:
        coc = a // b
        res = a % b
        return(coc, res)
try:
    print(division(10, 0))
except Exception as e:
    print(e, "\n", type(e)) #Hasta acá el tema de Manejo de excepciones
'''