from Agenda import agenda 
import os

def menu():
    print("-----------------")
    print("MENU DE OPCIONES:")
    print(" 1) Añadir contacto.")
    print(" 2) Mostrar lista de contacto.")
    print(" 3) Buscar contado.")
    print(" 4) Editar contacto.")
    print(" 5) Cerrar agenda.")

def clean_screen():
    print("----")
    tecla = input("Precione cualquier tecla para salir")
    os.system('cls')


mi_agenda = agenda()
while True:
    menu()
    option = int(input("opcion = "))
    if option == 1:
        os.system('cls')
        mi_agenda.add_contact()
        clean_screen()
    elif option == 2:
        os.system('cls')
        mi_agenda.show_contacts()
        clean_screen()
    elif option == 3:
        os.system('cls')
        mi_agenda.seach_contact()
        clean_screen()
    elif option == 4:
        os.system('cls')
        mi_agenda.edit_contact()
        clean_screen()
    elif option == 5:
        print("Ha salido del menu.")
        break
    else:
        print("La opcion ingresada es incorrecta!!")
