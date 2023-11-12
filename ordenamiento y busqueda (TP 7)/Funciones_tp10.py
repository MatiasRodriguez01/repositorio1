import random

def fill_random_list():
    lista = []
    for i in range(8):
        lista.append(random.randint(0,100))
    return lista


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

def show_dictionary(dictionary):
    for book in dictionary:
        counter = 1
        for key, values in book.items():
            if counter == 3:
                print(end= f"{key} : {values}.")
            else:
                print(end= f"{key} : {values}, ")
            counter += 1
        print(" ")