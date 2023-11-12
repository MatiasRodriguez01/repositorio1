#                                     PROGRAMACION I
#  TRABAJO PRACTICO N°6

import funciones_clase14
import numpy as np
import os

print("EJERCICIO 1:")
numbers = []
numbers = funciones_clase14.fill_numbers()
print("-----")
print(f"Lista = {numbers}")


print("-------------")
print("EJERCICIO 2:")
list_numbers = [3, 5, 7, 2, 5, 7, 8, 4]
print(f"Dada esta lista = {list_numbers}")
number = int(input("Ingrese el numero que desea eliminar de la lista: "))
list_numbers = funciones_clase14.delete_occurrence(list_numbers, number)


print("-------------")
print("EJERCICIO 3:")
lista_numbers = [3, 8, 6, 9, 4, 1, 5, 7]
print(f"Dada esta lista = {lista_numbers}")
print(f"La suma de los numeros de la lista es = {funciones_clase14.sum_list(lista_numbers)}")


print("-------------")
print("EJERCICIO 4:")
lista_numeros = []
lista_numeros = funciones_clase14.fill_random_list()
print(f"Dada esta lista = {lista_numeros}")
number = int(input("Ingrese un numero, para guardar una lista con numeros menores: "))
smaller_numbers = funciones_clase14.smaller_numbers(number, lista_numeros)
print(f"La lista con los numeros menores que {number} = {smaller_numbers}")


print("-------------")
print("EJERCICIO 5:")
lista_original = [8, 3, 45, 2, 8, 8, 3, 7, 45, 12, 2, 7]
print(f"Dada la siguiente lista = {lista_original}")
lista_con_tuplas = funciones_clase14.tuples_list(lista_original)
print(f"Tenemos una lista ordenada = {lista_con_tuplas}")


print("-------------")
print("EJERCICIO 6:")
print("Ingrese los nombres de los alumnos de nivel primario: ")
primary = list(funciones_clase14.names())
primary = list(set(primary)) 
print("-------------------------")
print("Ingrese los nombres de los alumnos de nivel primario: ")
secondary = list(funciones_clase14.names())
secondary = list(set(secondary))
print("-------------------------")
print(f"Alumnos de la primaria = {primary}")
print(f"Alumnos de la secundaria = {secondary}")
repeated_names, names_not_repeated = funciones_clase14.names_repeated(primary, secondary)
print(f"En ambos niveles se repiten los nombres = {repeated_names}")
print(f"Los nombres que no se repiten son = {names_not_repeated}")


print("-------------")
print("EJERCICIO 7:")
print("LLENE EL ARREGLO!!")
list_strings = funciones_clase14.strings()
print("-----------------")
funciones_clase14.strings_occurrence(list_strings)


print("-------------")
print("EJERCICIO 8:")
goles_equipos = funciones_clase14.inter_barrial()
for i in goles_equipos:
    print(goles_equipos)
print("/////////////////////////////////////")
for i in range(10):
    goles_anotados = 0
    goles_recibidos = 0
    puntos = 0
    partidos_ganados = 0
    partidos_perdidos = 0
    partidos_empatados = 0
    for j in range(10):
        if (i != j):
            goles_anotados = goles_equipos[i][j]
            goles_recibidos = goles_equipos[j][i]
            if (goles_anotados > goles_recibidos):
                puntos += 2
                partidos_ganados += 1
            elif (goles_anotados < goles_recibidos):
                partidos_perdidos += 1
            else:
                puntos += 1
                partidos_empatados += 1
    print("-------------------------------------")
    print(f"El EQUIPO {i+1} tuvo los siguientes resultados:")
    print(f"Triunfos = {partidos_ganados}")
    print(f"Derrotas = {partidos_perdidos}")
    print(f"Empates = {partidos_empatados}")
    print(f"La diferencia entre goles recibidos y anotados = {goles_anotados-goles_recibidos}")
    print(f"PUNTOS OBTENIDOS = {puntos}")


print("-------------")
print("EJERCICIO 9:")

memotest = [
    ('C1','C10','C7','C2'),
    ('C3','C6','C8','C5'),
    ('C9','C1','C4','C9'),
    ('C5','C10','C8','C4'),
    ('C7','C3','C6','C2')
]

matriz = [
    ('01','02','03','04'),
    ('05','06','07','08'),
    ('09','10','11','12'),
    ('13','14','15','16'),
    ('17','18','19','20')
]
while True:
    # IMPORTAMOS la funcion (numpy)
    # Y HACEMOS UN np.unique(matriz) PARA AGRUPAR TODOS LOS ELEMENTOS REPETIDOS DE LA MATRIZ
    elementos_unicos = np.unique(matriz)
    # SI TODOS LOS ELEMENTO DE LA MATRIZ SON (XX) ENTONCES HACEMOS UN (len) PARA VER SI HAY UN SOLO ELEMENTO
    if len(elementos_unicos) == 1: 
        break
    else:
        print("JUGEMOS AL MEMPTEST: ")
        print("---------------------")
        funciones_clase14.show_Matriz(matriz)
        print("---------------------")
        print("Eliga 2 de las cartas que se muestran para ver si hay coincidencias entre ellas: ")
        print("Si una carta fue tachada no se juega: ")
        carta1 = input("Carta 1 = ")
        carta2 = input("Carta 2 = ")
        x1, x2 = funciones_clase14.indices(matriz, carta1, carta2)
        if (carta1 not in elementos_unicos) or (carta2 not in elementos_unicos):
            os.system('cls')
            print("---------------------")
            print("UNA DE LAS CARTAS YA FUE ENCONTRADA, O LA CARTA NO EXISTE")
            continue
        else:
            os.system('cls')
    
        if x1 == x2:
            print("---------------------")
            print("LAS CARTAS NO PUEDEN SER LAS MISMA!!")
        elif memotest[x1[0]][x1[1]] == memotest[x2[0]][x2[1]]: 
            print("---------------------")
            print("SE ENCONTRARON COINCIDENCIAS ")
            matriz[x1[0]][x1[1]] = "XX"
            matriz[x2[0]][x2[1]] = "XX"
        else:
            print("---------------------")
            print("NO SE ENCONTRARON COINCIDENCIAS ")
os.system('cls')
print("---------------------")
funciones_clase14.show_Matriz(matriz)
print("---------------------")
print("SE TERMINO EL JUEGO!!")


print("-------------")
print("EJERCICIO 10:")
matriz_cuadrada = funciones_clase14.fill_matriz(3)
print("Dada la siguiente matriz cuadrada:")
funciones_clase14.show_Matriz(matriz_cuadrada)
diagonal_principal, diagonal_inversa = funciones_clase14.main_and_inverse_diagonal(matriz_cuadrada, 3)
print(f"Diagonal principal = {diagonal_principal}.")
print(f"Diagonal inversa = {diagonal_inversa}.")


print("-------------")
print("EJERCICIO 11:")
dictionary = {'Euro':'€', 'Dollar':'$', 'Yen':'¥', 'Won':'₩','Libra':'£','Yuan':'£'}
while True:
    divisa = input("Ingrese una divisa, para mostrar su simbolo: ")
    divisa = divisa.lower().capitalize()
    if (divisa in dictionary): 
        print("-----------------")
        print(f"El simbolo de {divisa} es {dictionary[divisa]}." )
    else:
        print("-----------------")
        print("La divisa ingresada no se encuentra en el diccionario.")
    option = funciones_clase14.exit()
    if (option == "s" or option == "S"):
        break

print("-------------")
print("EJERCICIO 12:")
user = {}
user = funciones_clase14.user_dictionary(user)
print("----")
persona = (f"{user['Nombre']} tiene {user['Edad']} años, vive en {user['Direccion']} y su número de teléfono es {user['Telefono']}.")
print(persona)


print("-------------")
print("EJERCICIO 13:")
fruits = {'naranja' : 300 ,'manzana' : 250 , 'banana' : 400 ,'durazno' : 290 ,'mandarina' : 320 , 'limon' : 200}
while True:
    print("--------------------------")
    fruit = input("Ingrese la fruta que desee comprar: ")
    fruit = fruit.lower()
    kl = int(input("Ingrese los kilos que va a llevar: "))
    precio = 0
    print("--------------------------")
    if (fruit in fruits):
        precio = fruits[fruit] * kl
        print(f"Deberá pagar ${precio} por los {kl} kilos de {fruit}.")  
    else:
        print("la fruta no esta en la lista")
    option = funciones_clase14.exit()
    if (option == "s" or option == "S"):
        break
