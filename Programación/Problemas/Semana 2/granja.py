'''
En una granja se crıan un numero de V - Vacas, A - Aves (pollos y
gallinas) y E - escorpiones. Las vacas estan encerradas en un corral de
N × M metros cuadrados, las aves en un galpon y los escorpiones en
vitrinas. Para cada subproblema utilice solo los datos que necesite
1) Si una vaca necesita K metros cuadrados de pasto para producir X
litros de leche por día, ¿cuantos litros de leche se producen por
semana en la granja?.
2) Si 1/3 de las aves que hay en la granja son gallinas, y la mitad de las
gallinas ponen 1 huevo cada 3 dıas y la otra mitad 1 huevo cada 5
dıas, ¿en un mes cuantos huevos producen? (1 mes ≡ 30 d ́ıas).
3) Si los escorpiones de la granja se venden a China, y hay escorpiones
de tres diferentes tama ̃nos: peque ̃nos (con un peso de 20 gramos),
medianos (con un peso 30 gramos) y grandes (con un peso de 50
gramos), ¿cuantos kilos de escorpiones se pueden vender sin que
decrezca la poblaci ́on a menos de 2/3?.
4) Al granjero se le daño el corral y no sabe si volver a cercar el corral
con madera, alambre de p ́uas o poner reja de metal. Si va a cercar
con madera debe poner 4 hileras de tablas, con varilla 8 hileras y con
alambre solo 5 hileras,  ́el quiere saber que es lo menos costoso para
cercar si sabe que el alambre de púas vale P por metro, las tablas a Q
por metro y las varillas S por metro. Dado el tama ̃no del corral y los
precios de los elementos, ¿cu ́al cerramiento es el m ́as económico?.
'''
#Punto 1:
def litros_leche(k,x,m,d,v):
    #sea m los metros cuadrados del corral
    #sea d los litros de leche producidos en un determinado tiempo
    #sea v el número de vacas que hay en la granja
    if (v * d * k) > m:
        x = 0
        return v * x
    else:
        x = d * k
    return v * x

k = float(input("Metros cuadrados de pasto que necesita una vaca para producir leche por unidad de tiempo: "))
x = float(input("Litros de leche que produce una vaca por unidad de tiempo: "))
m = float(input("Metros cuadrados que tiene el corral: "))
d = float(input("Periodo de tiempo en el cual producirá leche: "))
v = float(input("Cantidad de vacas con las que cuenta en su granja: "))

if (v * d * k) > m :
    print("En el corral y tiempo elegido, se producirán: ", (litros_leche(k,x,m,d,v)), "litros de leche")
else:
    print("En el corral y tiempo elegido, se producirán: ", (litros_leche(k,x,m,d,v)), "litros de leche")

#Punto 2:
