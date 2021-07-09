'''
La tienda Euro-Town inaugura sus nuevos almacenes en Ecuador y requieren un
análisis de precios para su campaña comercial.

Inicialmente se conoce que, si le restan $4 (USD) al valor de un producto
de hogar, se completa dos veces el valor de un producto de
papelería, y que, con el total invertido por la compra de un combo
especial (un producto de hogar y un producto de papelería), es posible adquirir
hasta 5 unidades de un producto de limpieza. La administración ha definido que
los valores de los productos siempre son netos y no contienen céntimos.

Euro -Town categoriza sus productos acordes a sus precios. En sus tiendas, un
producto de nivel uno, corresponde al clasificado en un rango de precios
entre $0 y $20. Los que son mayores a $20 y máximo hasta $30 dólares se
clasifican en el nivel dos. Si el rango de precio oscila entre $31 y $50 USD se
le asigna el nivel tres. En el caso que el precio sea mayor a los
anteriores, se le asigna automáticamente el nivel cuatro.

La empresa requiere de un programa que, de acuerdo con el valor capturado para
un producto de papelería, se imprima por pantalla los valores de todos los
productos mencionados, así mismo, imprima el nombre del nivel generado para el
producto de limpieza.

Entrada

Un número que represente el precio para un producto de papelería.

Salida

En la primera línea y separados por un espacio, cada uno de los precios de los
productos de las secciones de papelería, hogar y limpieza (en este orden), y en
la segunda línea, un texto que describa el nombre del nivel obtenido para el
producto de limpieza.
'''

x = int(input("ingrese el precio del producto de papelería: ")) # "x" es el valor del producto de papelería y es entero por politicas de la tienda

while x < 0: #Este while es para cuando el usuario mete un número negativo
    print("Ingrese un valor válido")
    x = int(input("ingrese el precio del producto de papelería: "))

y = (2 * x) + 4 # "y" es el valor del producto de hogar

z = (x + y)//5 # "z" es el valor del producto de limpieza

if z <= 20:

    categoria = str("uno")

elif z <= 30:

    categoria = str("dos")

elif z <= 50:

    categoria = str("tres")

else:

    categoria = str("cuatro")


print(x," ", y," ", z)
print(categoria)
