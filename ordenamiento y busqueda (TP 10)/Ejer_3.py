import Fcs_ordenamiento as Fun
import Funciones_tp10 as f

def orden_dictionary(element, dictionary):
    for i in range(len(dictionary)):
        for i in range(1, len(dictionary)):
            if dictionary[i-1][element] > dictionary[i][element]:
                dictionary[i-1], dictionary[i] = dictionary[i], dictionary[i-1]



print("EJERCICIO 3:")
list_dictionary = [
    {'titulo' : 'El señor de los anillos', 'autor' : 'J.R.R.Tolkien', 'año' : 1955},
    {'titulo' : 'Harry Potter y la piedra filosofal', 'autor' : 'J.K. Rowling', 'año' : 1997},
    {'titulo' : 'Las crónicas de Narnia: El león, la bruja y el armario', 'autor' : 'C.S. Lewis', 'año' : 1950},
    {'titulo' : 'Juego de tronos(Canción de hielo y fuego, libro 1)', 'autor' : 'George R.R. Martin', 'año' : 1996},
]
print("Lista original:")
f.show_dictionary(list_dictionary)

while True:
    print("-------------------------")
    print("Ingrese la opcion por la cual ordenara la lista de diccionarios: ")
    print("1) Por titulo.")
    print("2) Por autor.")
    print("3) Por año de publicacion")
    option = int(input("opcion : "))
    if option == 1 or option == 2 or option == 3:
        break

if (option == 1):
    print("Lista ordenada, por el nombre de auto: ")
    orden_dictionary('titulo', list_dictionary)
    f.show_dictionary(list_dictionary)
elif (option == 2):
    print("Lista ordenada, por el titulo del libro: ")
    orden_dictionary('autor', list_dictionary)
    f.show_dictionary(list_dictionary)
elif (option == 3):
    print("Lista ordenada, por el año de creacion")
    orden_dictionary('año', list_dictionary)
    f.show_dictionary(list_dictionary)
