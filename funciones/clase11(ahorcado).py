# 26/9/23                           PROGRAMACION 1 

# AHORCADO 

import funciones_clase11
import os

# Esta es a lista del ahorcado
list_word = ["maradona", "benzema", "ronaldinho", "mbappe", "ronaldo nazario"]

# con esta variable mostraremos el contador de cuantas palabra adivino
hits = 0

# Con este bucle for, recorrera cada elemento de la lista
for i in list_word:
    # insertamos los intentos que tiene el usuario
    intens = 6

    # con esta funcion llamamos a una funcion que nos llena la variable de astericos
    # y se va modicandon segun el programa
    word = funciones_clase11.fill_asterisks(i)
    print("")

    # En el siguiente condicional, haremos un condicional para cada elemento de la lista
    if i == "maradona":
        while True:
            # con la variable (word_or_letter) asignamos una letra del nombre, o el nombre completo
            # el usuario entra 6 intentos para jugar
            os.system('cls')
            print("Adivine el siguiente jugador de futbol!")
            print("PISTA = Es uno de los mejores jugadores Argentinos y de la historia.")
            word_or_letter = funciones_clase11.fill_word_or_letter(word, intens)
            word_or_letter = word_or_letter.lower()

            # vamos a hacer un condicional si el usuario adivino el nombre del jugardor gano
            # de lo contrario sino ingrese el nombre entrara en el 'else'
            if word_or_letter == i:
                word = word_or_letter
            else:
                # con esta funcion agregamos la palabra ingresa por el usuario y vamos a modificar 
                # la variable con asteriscos
                word = funciones_clase11.fill_word_empty(word, word_or_letter, i)
            
            # con este condicional vamos a ver si el usuario adivino el jugador de futbol
            if word == i or word_or_letter == i:
                # si entro en esta condicion significa que adivino el jugador
                funciones_clase11.you_win(i)
                hits += 1
                funciones_clase11.go()
                break
            elif intens == 1:
                # si entro es porque el jugador se le terminaron los intentos y no adivino el jugador
                funciones_clase11.cero_intens()
                funciones_clase11.go()
                break
            # a medida que va avanzando el juego el programa restara los intentos del usuario
            intens -= 1
    elif i == "benzema":
        while True:
            # con la variable (word_or_letter) asignamos una letra del nombre, o el nombre completo
            # el usuario entra 6 intentos para jugar
            os.system('cls')
            print("Adivine el siguiente jugador de futbol!")
            print("PISTA = Jugador frances que jugo en el REAL MADRID.")
            word_or_letter = funciones_clase11.fill_word_or_letter(word, intens)
            word_or_letter = word_or_letter.lower()

            # vamos a hacer un condicional si el usuario adivino el nombre del jugardor gano
            # de lo contrario sino ingrese el nombre entrara en el 'else'
            if word_or_letter == i:
                word = word_or_letter
            else:
                # con esta funcion agregamos la palabra ingresa por el usuario y vamos a modificar 
                # la variable con asteriscos
                word = funciones_clase11.fill_word_empty(word, word_or_letter, i)
            
            # con este condicional vamos a ver si el usuario adivino el jugador de futbol
            if word == i or word_or_letter == i:
                # si entro en esta condicion significa que adivino el jugador
                funciones_clase11.you_win(i)
                hits += 1
                funciones_clase11.go()
                break
            elif intens == 1:
                # si entro es porque el jugador se le terminaron los intentos y no adivino el jugador
                funciones_clase11.cero_intens()
                funciones_clase11.go()
                break

            # a medida que va avanzando el juego el programa restara los intentos del usuario
            intens -= 1
    elif i == "ronaldinho":
        while True:
            # con la variable (word_or_letter) asignamos una letra del nombre, o el nombre completo
            # el usuario entra 6 intentos para jugar
            os.system('cls')
            print("Adivine el siguiente jugador de futbol!")
            print("PISTA = Jugador que hacia magia dentro de la cancha.")
            word_or_letter = funciones_clase11.fill_word_or_letter(word, intens)
            word_or_letter = word_or_letter.lower()

            # vamos a hacer un condicional si el usuario adivino el nombre del jugardor gano
            # de lo contrario sino ingrese el nombre entrara en el 'else'
            if word_or_letter == i:
                word = word_or_letter
            else:
                # con esta funcion agregamos la palabra ingresa por el usuario y vamos a modificar 
                # la variable con asteriscos
                word = funciones_clase11.fill_word_empty(word, word_or_letter, i)
            
            # con este condicional vamos a ver si el usuario adivino el jugador de futbol
            if word == i or word_or_letter == i:
                # si entro en esta condicion significa que adivino el jugador
                funciones_clase11.you_win(i)
                hits += 1
                funciones_clase11.go()
                break
            elif intens == 1:
                # si entro es porque el jugador se le terminaron los intentos y no adivino el jugador
                funciones_clase11.cero_intens()
                funciones_clase11.go()
                break

            # a medida que va avanzando el juego el programa restara los intentos del usuario
            intens -= 1
    elif i == "mbappe":
        while True:
            # con la variable (word_or_letter) asignamos una letra del nombre, o el nombre completo
            # el usuario entra 6 intentos para jugar
            os.system('cls')
            print("Adivine el siguiente jugador de futbol!")
            print("PISTA = Es la futura promesa del futbol.")
            word_or_letter = funciones_clase11.fill_word_or_letter(word, intens)
            word_or_letter = word_or_letter.lower()

            # vamos a hacer un condicional si el usuario adivino el nombre del jugardor gano
            # de lo contrario sino ingrese el nombre entrara en el 'else'
            if word_or_letter == i:
                word = word_or_letter
            else:
                # con esta funcion agregamos la palabra ingresa por el usuario y vamos a modificar 
                # la variable con asteriscos
                word = funciones_clase11.fill_word_empty(word, word_or_letter, i)
            
            # con este condicional vamos a ver si el usuario adivino el jugador de futbol
            if word == i or word_or_letter == i:
                # si entro en esta condicion significa que adivino el jugador
                funciones_clase11.you_win(i)
                hits += 1
                funciones_clase11.go()
                break
            elif intens == 1:
                # si entro es porque el jugador se le terminaron los intentos y no adivino el jugador
                funciones_clase11.cero_intens()
                funciones_clase11.go()
                break

            # a medida que va avanzando el juego el programa restara los intentos del usuario
            intens -= 1
    else:
        
        while True:
            # con la variable (word_or_letter) asignamos una letra del nombre, o el nombre completo
            # el usuario entra 6 intentos para jugar
            os.system('cls')
            print("Adivine el siguiente jugador de futbol!")
            print("PISTA = En su momento le decian el fenomeno.")
            word_or_letter = funciones_clase11.fill_word_or_letter(word, intens)
            word_or_letter = word_or_letter.lower()

            # vamos a hacer un condicional si el usuario adivino el nombre del jugardor gano
            # de lo contrario sino ingrese el nombre entrara en el 'else'
            if word_or_letter == i:
                word = word_or_letter
            else:
                # con esta funcion agregamos la palabra ingresa por el usuario y vamos a modificar 
                # la variable con asteriscos
                word = funciones_clase11.fill_word_empty(word, word_or_letter,i)
            
            # con este condicional vamos a ver si el usuario adivino el jugador de futbol
            if word == i or word_or_letter == i:
                # si entro en esta condicion significa que adivino el jugador
                funciones_clase11.you_win(i)
                hits += 1
                key = input("PRESION ENTER PARA TERMINAR ")
                os.system('cls')
                break
            elif intens == 1:
                # si entro es porque el jugador se le terminaron los intentos y no adivino el jugador
                funciones_clase11.cero_intens()
                key = input("PRESION ENTER PARA TERMINAR ")
                os.system('cls')
                break

            # a medida que va avanzando el juego el programa restara los intentos del usuario
            intens -= 1

print("SE TERMINO EL JUEGO!!")
print(f"Usted acerto {hits} de los {len(list_word)} jugadores de futbol")