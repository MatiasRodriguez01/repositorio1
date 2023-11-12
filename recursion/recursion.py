#  17/10/23                                 PROGRAMACION
#  RECURSION

import funciones_recursion
import os

hills = 3
options = [1, 2, 3]
minutos = [3, 5, 7]


print("EJERCICIO 1:")
funciones_recursion.linea()
while (hills != 0):
    option = funciones_recursion.caminos_a_elegir(hills, options)
    while option not in options:
        os.system('cls')
        funciones_recursion.linea()
        print("opcion incorrecta!!")
        option = funciones_recursion.caminos_a_elegir(hills, options)
        if option not in options:
            os.system('cls')
    funciones_recursion.linea()
    options, minutos, minute = funciones_recursion.opciones_a_elegir(option, options, minutos)
    funciones_recursion.laberinto(minute)
    funciones_recursion.linea()
    hills -= 1



funciones_recursion.linea()
print("EJERCICIO 2:")
'''
En el siguiente ejercicio necesitamos que el usuario ingrese un numero entero y que devuelva 
el numero mismo numero pero inverso. para eso necesitamos crear una funcion recursiva para que 
resiva un numero entero y devuelva el numero inverso.
'''
numero = input("Ingrese un numero, para saber su inverso: ")
print("El numero inverso es = ", funciones_recursion.f(numero))