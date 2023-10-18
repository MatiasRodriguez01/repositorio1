

# EJERCICIO 1:

def fill_numbers():
    lista = []
    print("VAMOS A LLENAR UNA LISTA CON NUMEROS")
    while True:
        number = int(input("Ingrese un numero(ingrese 0 para salir): "))
        if number == 0:
            break
        else:
            lista.append(number)
    return lista