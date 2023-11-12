import funciones_clase13 as funciones

members = {
        1: {"nombre": "Amanda Núñez", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True},
        2: {"nombre": "Bárbara Molina", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True},
        3: {"nombre": "Lautaro Campos", "fecha_ingreso": "17/03/2009", "cuota_al_dia": False}
    }

while True:
    funciones.menu()
    option = int(input("opcion: "))
    if option == 1:
        print("------------------------")
        print("CLUB:")
        print(f"En el club hay {len(members)} socios.")
        funciones.clean_screen()
    elif option == 2:
        print("------------------------")
        funciones.debt(members)
        funciones.clean_screen()
    elif option == 3:
        print("------------------------")
        funciones.new_date(members)
        funciones.clean_screen()
    elif option == 4:
        print("------------------------")
        funciones.delete_membre(members)
        funciones.clean_screen()
    elif option == 5:
        print("------------------------")
        funciones.show_membres(members)
        funciones.clean_screen()
    elif option == 6:
        print("Ha salido del menu.")
        break
    else:
        print("Opcion incorrecta!!.")


