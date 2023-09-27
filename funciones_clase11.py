
import os

# con esta funcion usted asignara una letra o palabra por tecla 
# y mostrara los intentos que le quedan para jugar  
def fill_word_or_letter(x, intentos):
    print(x)
    print(f"Te quedan {intentos} intentos.")
    return input("Ingrese una letra para adivinar al jugador o ingrese el nombre si adivinaste: ")


# con esta funcion llenamos una palabra vacia
def fill_word_empty(palabra, letra,i):
    # con este bucle llenamos una palabra vacia
    # si la letra ingresada coincide con una de la palabra de la lista se asigna a la palabra vacia,
    # de lo contrario se llenara un guion bajo
    word_empty = ""
    for x in range(len(i)):
        if letra == i[x]:
            word_empty += letra
        else:
            word_empty += palabra[x]
    return word_empty

# con esta funcion llenamos una palabra vacia con asteriscos
def fill_asterisks(word):
    # llenamos una variables de asteriscos, con la misma cantidad de letra que tiene la palabra 
    # (Si la palabra tiene 8 letras, la variable contendra 8 asteriscos)
    palabra = ""
    for i in word:
        if i == " ":
            palabra += " "
        else:
            palabra += "_"
    return palabra

# con esta funcion el programa, mostrara mensajes avisando al usuario que adivino el jugador
def you_win(palabra):
    print("")
    print("FELICIDADES ADIVINO EL JUGADOR!!!!")
    print(f"El jugador es {palabra}")

# con esta funcion el programa, mostrara mensajes avisando al usuario que se le terminaron los intentos
def cero_intens():
    print("")
    print("SE TERMINARON LOS INTENTOS!!")
    print("NO ADIVINO EL JUGADOR DE FUTBOL!!")

# con esta funcion el usuario precionara enter para pasar al siguiente jugador 
# Limpiando pantalla de los anteriormente ejercutado
def go():
    key = input("SELECIONE ENTRE PARA PASAR AL SIGUIENTE JUGADOR ")
    os.system('cls')


