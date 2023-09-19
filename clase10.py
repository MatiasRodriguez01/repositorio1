#   19/9/2023                       programacion 1

import funciones

num = int(input("Ingrese un numero(ingrese 0 para salir): "))
while num != 0:
    add = (funciones.add_numbers(num))
    print(f"La suma =  {add}")
    num = int(input("Ingrese un numero(ingrese 0 para salir): "))