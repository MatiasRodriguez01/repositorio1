# 28/9/23                           PROGRAMACION 1

# TRABAJO PRACTICO N°5 

'''
Escribir una función que, dado un string, retorne la longitud de la última
 palabra. Se considera
que las palabras están separadas por uno o más espacios. También podría haber espacios al principio 
o al final del string pasado por parámetro.
'''

import funciones_clase12
import os
import random
import math

print("EJERCICIO 1:")
dni = input("Ingrese su DNI, para verificar si es valido: ")
print(f"EL DNI es invalido? {funciones_clase12.quality_document(dni)}")

print("")
print("EJERCICIO 2:")
string = input("Ingrese una frase: ")
print( "La ultima palabra de la frase tiene ",funciones_clase12.quality_letter(string), " Letras.")


print("")
print("EJERCICIO 3:")
# Ingresamos el nombre completo
name = input("Ingrese su numbre completo: ")
# EL usuario ingresara el dni
dni = input("Ingrese su DNI: ")
# con este bucle validara si el DNI es correcto
while True:
    if funciones_clase12.quality_document(dni) == True:
        break

# Creamos varias variables para amacenar cada nombre y apellido del string
nombre1 = " " ; nombre2 = " " ; apellido = " "; identificacion = ""
nombre1,nombre2,apellido = funciones_clase12.registro(name)

# con esta funcion hacemos que nos den una identificacion 
identificacion = funciones_clase12.id(nombre1,apellido,dni)
# y al final mostramos los datos
print("------------------------------------------")
print("Nombre completo = ", name)
print("DNI = ", dni)
print("ID = ", identificacion)



print("")
print("EJERCICIO 4:")
number1, number2 = funciones_clase12.ingrese_numeros()
print(f"EL primero es multiplo del segundo??: {funciones_clase12.multiplos(number1, number2)}")


print("")
print("EJERCICIO 5:")
day = int(input("Ingrese cuantos dias desea saber la temperatura media: "))
for i in range(0,day):
        print("-------------------------")
        print(f"Es el dia {i+1}:")
        min = float(input("Ingrese la temperatura minima del dia: "))
        max = float(input("Ingrese la temperatura maxima del dia: "))
        print(f"La temperatura media del dia {i} es de {funciones_clase12.temp_mediun(max, min)}°")


print("")
print("EJERCICIO 6:")
word = input("ingrese una palabra: ")
val = funciones_clase12.espace_word(word)
print(val)


print("")
print("EJERCICIO 7:")
list_numbers = []
list_numbers = funciones_clase12.llenar_lista(list_numbers)
print(f"Dada los elementos de esta lista {list_numbers}")
smaller_number = 0; larger_number = 0
smaller_number, larger_number = funciones_clase12.element_max_and_min(list_numbers)
print(f"El elemento mayor de todos es = {funciones_clase12.element_max(list_numbers)}")


print("")
print("EJERCICIO 8:")
radio = int(input("Ingrese el radio, para saber el area y el perimetro de una circunferencia: "))
a , p = funciones_clase12.area_perimetro(radio)

print(f"El area de la circunceferencia es = {a}")
print(f"El perimetro de la circunferencia es = {p}")

print("")
print("EJERCICIO 9:")
print("Bienvenido!!!")
user = input("Ingrese su usuario para ingresar: ")
password = input("Ingrese su contraseña: ")
intents = 0

while (funciones_clase12.login(user.lower(), password.lower()) == False) and intents != 3:
    if intents == 0:
        #os.system('cls')
        print("-------------")
        print("Se ingresaron incorrectamente el usuario y la contraseña vuelva a ingresarlos nuevamente!")
        print("<<<<Ahora tienes 3 intentos>>>>")
    else:
        print("-------------")
        print("Se ingresaron incorrectamente el usuario y la contraseña vuelva a ingresarlos nuevamente!")  

    user = input("usuario = ")
    password = input("contraseña = ")
    intents += 1

if intents == 3:
    print("--")
    print("Lo sentimos, usted no ha podido iniciar seccion!!!")
else:
    print("--")
    print("Felicidades!!, usted ha iniciado seccion correctamente.")


print("")
print("EJERCICIO 10:")
print("Dada este diccionario de productos:")
carrito = {
    'producto1': {'precio': 100, 'descuento': 10},
    'producto2': {'precio': 50, 'descuento': 5},
    'producto3': {'precio': 200, 'descuento': 20}
}
print(carrito)
precio_final = funciones_clase12.aplicar_descuento(carrito)
print(f"EL precio final del carrito de producto es de ${precio_final}.")

print("")
print("EJERCICIO 11:")

print("")
print("EJERCICIO 12:")
word = input("Ingrese un palabra o frase: ")
dictionary = funciones_clase12.dicc_word(word)
print(dictionary)


print("")
print("EJERCICIO 13:")
print("Vamos a calcular el modulo de un VECTOR!")
print("Para eso necesitamos 2 valores: ")
element1 = float(input("Ingrese el valor componente 1: "))
element2 = float(input("Ingrese el valor componente 2: "))
vector = funciones_clase12.module(element1, element2)
print(f"El resultado es {vector}")

print("")
print("EJERCICIO 14:")
number = int(input("Ingrese un numero: "))
if funciones_clase12.primo(number):
    print(f"El numero {number} es un numero primo.")
else:
    print(f"El numero {number} no es un numero primo.")

print("")
print("EJERCICIO 15:")
number = int(input("Ingrese un numero, para saber el factoria de 0 hasta ese numero: "))
count_number = 0
for i in range(number+1):
    print(f"El factorial de {i} = {funciones_clase12.factorial(i)}")
    count_number += 1
print("---------------------")
print(f"Se han leido {count_number} numeros.")
print("Ha finalizado !!")

print("")
print("EJERCICIO 16:")
number = int(input("Ingrese un numero, grande: "))
digit = int(input("Ingrese un digito: "))
print(f"El digito ingresado se encuentra {funciones_clase12.encontrar_digito(number, digit)}")

print("")
print("EJERCICIO 17:")
mayor = 0
while True:
    print("------------------------------")
    number = int(input("Ingrese un numero, que sea primo: "))
    if funciones_clase12.primo(number):
        digit = int(input("Ingrese un digito que desea encontrar en el numero: "))
        print(f"La suma de los digitos del numero ingresado es = {funciones_clase12.sum_digits(number)}")
        print(F"El numero que {digit} se encontro {funciones_clase12.encontrar_digito(number, digit)} veces dentro del numero {number}.")
        mayor = funciones_clase12.mayor_numero(number, mayor)
    else:
        break
print("------------------------------")
print(f"El mayor de los numeros ingresados fue el numero = {mayor}")
print("Usted ha salido!!!")
