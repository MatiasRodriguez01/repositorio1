
import funciones_clase14
import random
import os
import numpy as np

x = [{"nombre" : "matias rodriguez", "telefono" : "63425343", "correo" : "matiasrodriguez3002@gmail.com"},
     {"nombre" : "rodrigo rodriguez", "telefono" : "63425343", "correo" : "rodrigo10@gmail.com"},
     {"nombre" : "jesus rodriguez", "telefono" : "63425343", "correo" : "jesurodriguez78@gmail.com"}]

contador = 1
for diccionarios in x:
    print(f"contacto {contador} = ", end = "")
    for i, j in diccionarios.items():
        print(end = F"{i} : {j} ") 
    print(" ")
    contador += 1

print("--")
option = (input("Ingrese el nombre, telefono o correo para buscar ese contacto: "))


for diccionarios in x:
    for value in diccionarios.values():
        if (option in value):
            print(diccionarios)
            break


