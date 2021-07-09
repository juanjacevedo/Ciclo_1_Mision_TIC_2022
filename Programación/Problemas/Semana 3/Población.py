'''En 2022 el pa ́ıs A tendr ́a una poblaci ́on de 25 millones de habitantes
y el pa ́ıs B de 18.9 millones. Las tasas de crecimiento anual de la
poblaci ́on ser ́an de 2% y 3% respectivamente. Desarrollar un
programa que imprima el a ̃no en que la poblaci ́on del pa ́ıs B superar ́a
a la de A.'''

inicio = 2022
poblacion_A = 25000000
poblacion_B = 18900000
tasa_crecimiento_A = 0.02
tasa_crecimiento_B = 0.03


while poblacion_B < poblacion_A:

    poblacion_B = poblacion_B + poblacion_B * tasa_crecimiento_B

    poblacion_A = poblacion_A + poblacion_A * tasa_crecimiento_A

    inicio += 1

    print("En el año", inicio, " la población de B será", end = " ")
    print(int(poblacion_B), " y la de A será", end = " ")
    print(int(poblacion_A))


'''print("En el año", inicio, " la población de B será", end = " ")
print(int(poblacion_B), " y la de A será", end = " ")
print(int(poblacion_A))'''
