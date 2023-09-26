print("Ingrese una de las siguientes opciones")
print("1) juego de numero")
print("2) juego de numero")
option = int(input("Ingrese su opcion: "))
if (option == 1): 
    odd_counter = 0
    even_counter = 0
    while True:
        number = int(input("Ingrese un numero(Ingrese 0 para salir): "))
        if number == 0:
            break
        elif number % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    print(f"Se ingresaron un total de {even_counter} numeros pares.")
    print(f"Se ingresaron un total de {odd_counter} numeros impares.")
elif option == 2:
    word = input("Ingrese una frase o palabra: ")
    word = word.upper()
    vowel_A = 0
    vowel_E = 0
    vowel_I = 0
    vowel_O = 0
    vowel_U = 0
    for i in word:
        if i == "A":
            vowel_A += 1
        elif i == "E":
            vowel_E += 1
        elif i == "I":
            vowel_I += 1
        elif i == "O":
            vowel_O += 1
        elif i == "U":
                vowel_U += 1
    print("La frase o palabra contiene: ")
    print(vowel_A, " vocales A")
    print(vowel_E, " vocales E")
    print(vowel_I, " vocales I")
    print(vowel_O, " vocales O")
    print(vowel_U, " vocales U")