'''
En la tienda de don José, llego el proveedor de productos con el surtido para la actual semana. Luis, su ayudante, tiene la tarea de acomodarlos en el estante y sumar su cantidad según su tipo de acuerdo con la secuencia de producto en la que don José se los está pasando.

Para dejar clara la estrategia, don José le indica a Luis un ejemplo: Luis, si le paso dos panes, usted suma dos unidades a los panes, si le paso la pera, usted suma una unidad a la pera, si al avanzar le vuelvo a pasar panes, suma por separado, un pan y así sucesivamente. Al ser cientos de productos, Luis requiere ayuda con un programa que capture sus nombres de acuerdo con el orden en que don José se los pasa y que como resultado muestre la cantidad desagregada para cada uno de ellos.



Entrada

Como entrada se debe capturar la secuencia de los nombres (separados por un espacio) de los productos que recibe Luis según el orden que don José los entrega.

Salida

Una línea, con los nombres discriminados de la secuencia de cada producto según fueron recibidos y en la siguiente, la correspondiente cantidad acumulada por producto según su secuencia. En ambos casos, separados por un espacio.
'''

lista = []
resultado = []
producto = input()
producto = producto.split()
bandera = True
i = 0
contador = 1
while bandera:
    if i + 1 == len(producto):
        bandera = False
        lista.append(producto[i])
        resultado.append(str(contador))   
    elif producto[i] == producto[i+1]:
        i += 1  
        contador += 1
    else:
        lista.append(producto[i])
        resultado.append(str(contador))
        contador = 1
        i += 1
lista =  ' '.join(lista)
resultado = ' '.join(resultado)

print(lista)
print(resultado)

'''
lista_llamadas = input("ingrese lista: ").split(" ")
lista_llamadas.append("")
anterior, M = "",0
LIST_MH = []
LIST_VARMH = []
for i in range(len(lista_llamadas)):
    var = lista_llamadas[i]
    if var!=anterior:
        LIST_VARMH.append(str(M))
        LIST_MH.append(var)
        M=1
    else: M+=1
    anterior = var  
LIST_VARMH.pop(0)
LIST_MH.pop()
print(" ".join(LIST_MH) + "\n" +  " ".join(LIST_VARMH))
'''