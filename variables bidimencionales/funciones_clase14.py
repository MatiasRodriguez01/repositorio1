
import random

def fill_random_list():
    lista = []
    for i in range(8):
        lista.append(random.randint(0,100))
    return lista

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


# EJERCICIO 2:
def delete_occurrence(lista, number):
    if number in lista: 
        lista.remove(number)
        print(f"Se elimino la primera ocurrencia del numero {number} en la lista.")
        print("-------------")
        print(f"lista = {lista}")
    else:
        print("El numero no fue encontrado en la lista.")
    return lista


# EJERCICIO 3:
def sum_list(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma


# EJERCICIO 4:
def smaller_numbers(numero, lista):
    menores = []
    for i in lista:
        if i < numero:
            menores.append(i)
    return menores


# EJERCICIO 5:
def tuples_list(lista1):
    lista2 = []
    for i in lista1:
        if lista2 == []:
            count = 0
            tuppla_numero = ()
            for j in lista1:
                if (i == j):
                    count += 1
            tuppla_numero = (i, count)
            lista2.append(tuppla_numero)
            continue
        else:
            no_existe = True
            for j in lista2:
                if (i == j[0]):
                    no_existe = False
                    break
            if no_existe:
                count = 0
                tuppla_numero = ()
                for j in lista1:
                    if (i == j):
                        count += 1
                tuppla_numero = (i, count)
                lista2.append(tuppla_numero)
    return lista2

# EJERCICIO 6:

def names():
    lista = []
    while True:
        nombre = input("Ingrese un nombre, ingrese (x) para salir: ")
        if (nombre == "x"):
            break
        else:
            lista.append(nombre)
    return lista

def names_repeated(lista1, lista2):
    repetidos = []
    no_repetidos = []
    for i in lista1:
        if i in lista2:
            repetidos.append(i)
        else:
            no_repetidos.append(i)
    return repetidos, no_repetidos


# EJERCICIO 7:

def strings():
    lista = []
    for i in range(50):
        string = input(f"Ingrese el string N°{i+1}: ")
        lista.append(string)
    return lista


def strings_occurrence(lista):
    x = []
    for i in lista:
        if (i not in x):
            ocurrencias = 0
            for j in lista:
                if (i == j):
                    ocurrencias += 1
            x.append(i)
            print(f"El string {i} tiene {ocurrencias} ocurrencias.")


# EJERCICIO 8:
def inter_barrial():
    lista1 = []
    lista2 = []
    for equipos in range(10):
        for partido in range(10):
            #print("------")
            #goles = input(f"Ingrese los goles que hizo el equipo {equipos+1} en el partido {partido+1}: ")
            goles = random.randint(0,10)
            lista2.append(goles)
        lista1.append(lista2)
        lista2 = []
    return lista1


# EJERCICIO 9
def show_Matriz(matriz):
    for filas in matriz:
        for columnas in filas:
            print(end = f"| {columnas} ")
        print("|")


def indices(matriz, elemento1, elemento2):
    x1 = []
    x2 = []
    for filas in range(5):
        for columnas in range(4):
            if elemento1 == matriz[filas][columnas]:
                x1 = [filas, columnas]
            if elemento2 == matriz[filas][columnas]:
                x2 = [filas, columnas]
    return x1, x2


# EJERCICIO 10
def fill_matriz(tamanio):
    matriz = []
    for filas in range(tamanio):
        x =  []
        for columnas in range(tamanio):
            elemento = random.randint(0,9)
            x.append(elemento)
        matriz.append(x)
    return matriz

def main_and_inverse_diagonal(matriz, tamanio):
    diagonal1 = []
    diagonal2 = []
    
    for filas in range(tamanio):
        for columnas in range(tamanio):
            # DIAGONAL PRINCIPAL
            if (filas == columnas):
                diagonal1.append(matriz[filas][columnas])
            # DIAGONAL INVERSA
            if (filas + columnas) == (tamanio-1):
                diagonal2.append(matriz[filas][columnas])
    # DEVOLVEMOS LAS 2 DIAGONALES 
    return diagonal1, diagonal2


# EJERCICIO 11:


# EJERCICIO 12: 
def user_dictionary(user):
    print("¡BIENVENIDO USUARIO!")
    print("Ingrese sus datos: ")
    aux = {}
    name = input("Ingrese su numbre: ")
    name = name.title()
    aux = {"Nombre" : name}
    ####################
    user.update(aux)
    aux = {}
    age = int(input("Ingrese su edad: "))
    aux = {"Edad" : age}
    ####################
    user.update(aux)
    aux = {}
    address = input("Ingrese su direccion: ")
    address = address.title()
    aux = {"Direccion" : address }
    ####################
    user.update(aux)
    aux = {}
    phono = input("Ingrese su numero de telefono: ")
    aux = {"Telefono" : phono}
    ####################
    user.update(aux)
    return user


# EJERCICIO 13:
def exit():
    print("--------------------------")
    print("Si desea salir ingrese (s).")
    print("Si desea continuar, pulse cualquier tecla.")
    return input()