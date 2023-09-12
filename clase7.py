# 29/8/23                                  PROGRAMACION 1
#           EJERCICIOS EN CLASE FOR - WHILE
#           TEMA: ESTRUCTURAS ITERATIVAS
#            
#EJERCICIO 1:

alphabet = ("abcdefghijklmnñopqrstuvwxyz")
officers = "12345"

print("BIENVENIDOS AL JUEGO DE ESTRATEGIO!! ")
corrigendum = int(input("Ingrese el corrimiento para los mensajes: "))
for x in officers:
    word = input(f"Ingrese un mensaje para el OFICIAL {x}: ")
    message = ""
    for i in word.lower():
        if i in alphabet:
            index = alphabet.find(i)
            index_x = (index+corrigendum)%27
            message += alphabet[index_x]
        else:
            message += i

    print(f"MENSAJE PARA EL OFICIAL {x}: {message}")
    print("")

#EJERCICIO 2: 

number = int(input("Ingrese un numero(Para salir ingrese 0): "))
obb = 0
even = 0


while number != 0:
    for i in range(len(str(number))):
        digit = int((number % (10**(i+1)))/10**i)
        if digit % 2 == 0:
            even += 1
        else:
            obb += 1
    number = int(input("Ingrese un numero(Para salir ingrese 0): "))
    
print(f"Se ingresaron {even} digitos PARES")
print(f"Se ingresaron {obb} digitos IMPARES")