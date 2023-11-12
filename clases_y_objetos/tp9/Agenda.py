class agenda:

    def __init__(self):
        self.nombre = ""
        self.telefono = 0
        self.email = ""
        self.contacts = []        
    
    def add_contact(self):
        print("AGREGANDO CONTACTO: ")
        name = input("Ingrese el nombre del contacto: ")
        phone = int(input("Ingrese el numero del telefono: "))
        email = input("Ingrese el correo electrono: ")
        dictionary = {"nombre": name, "telefono": phone, "correo": email}
        self.modificar_contacs(dictionary)

    def seach_contact(self):
        if self.contacts == []:
            print("Lista vacia, primero llene la lista de contacto!!")
        else:
            seacher = (input("Ingrese el nombre, telefono o correo para buscar ese contacto: "))
            for dictionary in self.contacts:
                for value in dictionary.values():
                    if (seacher in value):
                        print(dictionary)
                        break

    def edit_contact(self):
        if self.contacts == []:
            print("Lista vacia, primero llene la lista de contacto!!")
        else:
            self.show_contacts()
            print("---")
            num = int(input("Ingrese el numero del contacto(no telefono), que desee cambiar: "))
            print("---")
            counter = 1
            for dictionary in self.contacts:
                for key in dictionary.keys():
                    if num == counter: 
                        option = input(f"Ingrese el nuevo {key}: ")
                        dictionary[key] = option
                counter += 1

    def modificar_contacs(self, element):
        self.contacts.append(element)

    def show_contacts(self):
        if self.contacts == []:
            print("Lista vacia, primero llene la lista de contacto!!")
        else:
            print("CONTACTOS: ")
            counter = 1
            for contact in self.contacts:
                print(f" Contacto {counter} = ", end = "")
                for key, value in contact.items():
                    if key != 'correo':
                        print(end= f"{key}: {value}, ")
                    else:
                        print(end= f"{key}: {value}.")
                counter += 1
                print("")

