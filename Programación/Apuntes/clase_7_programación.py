def valor_absoluto(x):
    if x >= 0:
        return x
    return -x
    '''
    valor = x if x >= 0 else -x
    return valor
    '''
    '''
    if x >= 0:
        valor = x
    else:
        valor = -x
    return valor
    '''
x = float(input("Ingrese un número real: "))
valor_abs = valor_absoluto(x)
#print("El valor absoluto de " + str(x) + " es " + str (valor_abs))
print("El valor absoluto de " + str(x), end = "") #El end = "" es para no dejar espacio
print("es " + str(valor_abs))

def maximo_dos_numeros(a,b):
    if a > b:
        return a
    return b

print(maximo_dos_numeros(4,8))

'''
a = float (input("Ingrese un número real: "))
b = float (input("Ingrese otro número real: "))
print("Entre los número ingresados, el mayor es " + str(maximo_dos_numeros(a,b)))
'''
def imprimir_numero(x):
    if x >= 0:
        #return x
        #print("+", end = "")
        print("+" + str(x))
    return x
print(imprimir_numero(8))

#pass

def condicional(p,q):
    if p == True and q == False:
        return False
    else:
        return True

print(condicional(True, False))
