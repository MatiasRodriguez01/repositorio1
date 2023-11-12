import os


# EJERCICIO 1

def limpiar_pantalla():
    x = input("Precione cualquier tecla para continuar: ")
    os.system('cls')

def fill_tuples():
    nombre = input("Ingrese el nombre del pasajero: ")
    nombre = nombre.lower()
    nombre = nombre.title()
    #############################
    while True:
        dni = int(input("Ingrese el dni del pasajero, de 7 o 8 digitos: "))
        if (len(str(dni)) == 8 or len(str(dni)) == 7):
            break
    #############################
    direccion = input("Ingrese su destino del viaje: ")
    direccion = direccion.lower()
    direccion = direccion.title()
    #############################
    print("--------------")
    return nombre, dni, direccion


def add_passengers(lista):
    while True:
        print("--------------------------------")
        print("INGRESE LOS DATOS DEL PASAJERO: ")
        name, document, direction = fill_tuples()
        pasajero = (name, document, direction)
        #########################################
        lista.append(pasajero)
        salir = input("Desea salir (s/n): ")
        if salir.lower() == "s":
            break
    print("--------------------------------")
    return lista


def add_locations(lista):
    ciudad = ""
    pais = ""
    localidad = ()
    while True:
        print("--------------------------------")
        print("INGRESE LOS DATOS DE LA CIUDAD: ")
        ciudad = input("Ingrese el nombre de una ciudad: ")
        ciudad = ciudad.lower()
        ciudad = ciudad.title()
        ###################################################
        pais = input("Ingrese el pais de la ciudad: ")
        pais = pais.lower()
        pais = pais.title()
        ###################################################
        localidad = (ciudad, pais)
        lista.append(localidad)
        salir = input("Desea salir (s/n): ")
        if salir.lower() == "s":
            break
    print("--------------------------------")
    return lista

def show_cities_or_countries(x, pasajeros, localidades):
    if (x == 3):
        print("LOS PASAJEROS QUE VIAJAN A:")
        for i in pasajeros:
            for j in localidades:
                if i[2] in j:
                    print(f"EL DNI {i[1]} va a viajar a la ciudad de {j[0]}")
    elif (x == 5):
        print("LOS PASAJEROS QUE VIAJAN A:")
        for i in pasajeros:
            for j in localidades:
                if i[2] in j:
                    print(f"EL DNI {i[1]} va a viajar a {j[1]}")

def numbers_of_travelers(x, pasajeros, localidades):
    if (x == 4):
        print("---------------------------------------------------------------------")
        print("Ingrese uno de las ciudades para saber cuanta gente va a viajar alli:")
        for x in localidades:
            print(f"* {x[0]}")
        option = (input("opcion: "))
        option = option.lower()
        option = option.title()
        count = 0
        for i in pasajeros:
            if option == i[2]:
                count += 1
        print("--------------------------------------")
        print(f"Unos {count} pasajeros viajan a {option}.")
    elif (x == 6):
        countries = []
        for lista in localidades:
            countries.append(lista[1])
        countries = set(countries)
        print("---------------------------------------------------------------------")
        print("Ingrese una de los paises para saber cuanta gente va a viajar alli:")
        for x in countries:
            print(f"* {x}")
        option = (input("opcion: "))
        option = option.lower()
        option = option.title()
        count = 0
        for i in pasajeros:
            for j in localidades:
                if i[2] == j[0]:
                    if j[1] == option:
                        count += 1
        print("--------------------------------------")
        print(f"Unos {count} pasajeros viajan a {option}.")


# EJERCICIO 2

def home(buy_list):
    home_list = []
    for i in buy_list:
        if (i[3] not in home_list):
            home_list.append(i[3])
        else:
            pass
    return home_list


# EJERCICIO 3:

def new_date(diccionario):
    socio = int(input("Ingrese el numero del socio para modificar su fecha: "))
    fecha = input("Ingrese la nueva fecha de ingreso para modificarla(En formato dd/mm/aaaa): ")
    for numero, datos in diccionario:
        if socio == numero:
            datos['fecha_ingreso'] = fecha
            if fecha == "13/08/2018":
                datos['fecha_ingreso'] = "14/08/2018"
    


def delete_membre(diccionario):
    socio = input("Ingrese el nombre y apellido del socio que desee dar de baja: ")
    for numero, datos in diccionario.items():
        if socio.title() in datos['nombre']:
            del diccionario[numero]

def debt(diccionario):
    socio = int(input("Ingrese el numero del socio para ver si pago las coutas adeudadas: "))
    if diccionario[socio]['cuota_al_dia'] == False:
        print(f"EL socio N°{socio} no ha pagado todas las coutas!!.")
    else:
        print(f"EL socio N°{socio} esta al dia con las coutas.")

def show_membres(diccionario):
    for numero, datos in diccionario.items():
        print(f"socio N°{numero}, {datos}")

def clean_screen():
    tecla = input("Ingrese una tecla para salir ")
    os.system('cls')

def menu():
    print("------------------------")
    print("MENU:")
    print("1) Informar la cantidad de socios del club.")
    print("2) Ver si un socio ha pagado todas las cuotas adeudadas.")
    print("3) Modifcar la fecha de ingreso de un socio.")
    print("4) Dar de baja a un socio.")
    print("5) Imprimer el listado de socios completo.")
    print("6) Salir.")


'''
def add_member(diccionario):
    print("Iscriba un nuevo socio: ")
    socio = {}
    nombre = input("Ingrese su nombre: ")
    fecha = input("Ingrese a fecha de ingreso, en formato dd/mm/aaaa: ")
    cuota = input("Esta al dia con la cuota(si/no): ")

    socio['nombre'] = nombre
    socio['fecha_ingreso'] = fecha
    socio['cuota_al_dia'] = (cuota.lower() == "si")

    n = len(diccionario) + 1
    nuevo = {n : socio}
    return nuevo
'''