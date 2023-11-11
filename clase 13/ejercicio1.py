import funciones_clase13
import os

while True:
    print("--------------------------------------")
    print("MENU")
    print("Ingrese una de las opciones: ")
    print("1) Agregar pasajeros.")
    print("2) Agregar ciudades.")
    print("3) Dado el DNI de un pasajero, ver a qué ciudad viaja.")
    print("4) mostrar la cantidad de pasajeros que viajan a una determinada ciudad.")
    print("5) Dado el DNI de un pasajero, ver a qué país viaja.")
    print("6) mostrar cuántos pasajeros viajan a ese país.")
    print("7) Salir del programa.")
    print("-----------------------")
    menu = int(input("Opcion: "))
    if (menu == 1):
        os.system('cls')
        passengers = []
        passengers = funciones_clase13.add_passengers(passengers)
        print(passengers)
        funciones_clase13.limpiar_pantalla()
    elif (menu == 2):
        os.system('cls')
        locations = []
        locations = funciones_clase13.add_locations(locations)
        print(locations)
        funciones_clase13.limpiar_pantalla()
    elif (menu == 3):
        os.system('cls')
        funciones_clase13.show_cities_or_countries(menu, passengers, locations)
        funciones_clase13.limpiar_pantalla()
    elif (menu == 4):
        os.system('cls')
        funciones_clase13.numbers_of_travelers(menu, passengers, locations)
        funciones_clase13.limpiar_pantalla()
    elif (menu == 5):
        os.system('cls')
        funciones_clase13.show_cities_or_countries(menu, passengers, locations)
        funciones_clase13.limpiar_pantalla()
    elif (menu == 6):
        os.system('cls')
        funciones_clase13.numbers_of_travelers(menu, passengers, locations)
        funciones_clase13.limpiar_pantalla()
    elif (menu == 7):
        break
print("Ha salido del programa")

