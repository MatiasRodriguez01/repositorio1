import random

'''
El programa pedira que el usuario ingrese una palabra que sea palindromo para ingresar al juego
'''

# Con este bucle while, ingresamos al juego 
print("BIENVENIDO AL JUEGO!!")
while True:

    #una vez que ingresamos el programa le pedira al usuario un palabra
    print("------------------------------------------------------------------")
    print("PARA INGRESAR AL JUEGO INGRESE UNA PALABRA QUE SEA PALINDROMO: ")
    word = input("Ingrese su palabra(Ingrese 0 para salir del juego): ")
    equals_letter = 0
    reverse_word = ""
    guess = False

    # Si el usuario ingreso un 0, se cierra el juego. si el usuario ingreso una palabra entra al condicional
    if (word != "0"):

        # una vez dentro, el programa asignara la misma palabra pero alrevez con un bucle for
        for i in range(len(word)-1,-1,-1):
            reverse_word += word[i]
        
        # con este if comparara la 2 palabra para ver si es palindromo
        if (word == reverse_word):
            # Entra en esta sentencia significa que entro al juego, ahora tendra 5 intentos para acertar el numero
            print("FELICIDADES!!!")
            print("La palabra es palindromo, PODES JUGAR!!")
            print("Vas a tener 5 intentos para ganar, SINO perdera el juego!!")
            print("")
            random_number = random.randint(0,100)
            attemps = 0
            # En el siguiente bucle 
            # 
            while True:
                if attemps < 5:
                    user_number = int(input("Ingrese un numero, entre el 0 y el 100: "))
                    attemps += 1
                    if (user_number > random_number):
                        print("EL numero es mayor!")
                        continue
                    elif (user_number < random_number):
                        print("El numero es menor!")
                        continue
                    else:
                        print("")
                        print("FELICIDADES ADIVINASTE EL NUMERO!!!!")
                        break
                else:
                    print("PERDISTE!!, SE AGOTARON TUS INTENTOS!!")
                    break
        else:
            # Si entra en el else 
            print("La palabra ingresada no es palindromo!!!!")
            print("INGRESE OTRA!!")
            continue
        
    else:
        break
print("¡¡GRACIAS POR JUGAR!!")
    