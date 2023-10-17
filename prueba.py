import funciones_clase12
import math
import os
import random

# ejercicio 12
'''
for i in range(0,11):
    print(f"El numero {i} es primo? {funciones_clase12.primo(i)}")

'''

def aplicar_descuento(carrito):
    total = 0
    for producto in carrito:
        precio = carrito[producto]['precio']
        descuento = carrito[producto]['descuento']
        precio_final = precio - (precio * descuento / 100)
        total += precio_final
    return total



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