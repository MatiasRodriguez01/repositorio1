# 29/8/23                                  PROGRAMACION 1
#           EJERCICIOS EN CLASE FOR - WHILE
#           TEMA: ESTRUCTURAS ITERATIVAS
#           nueva rama git 
#EJERCICIO 1:

abecedario = ("abcdefghijklmnñopqrstuvwxyz")
oficiales = "12345"

print("BIENVENIDOS AL JUEGO DE ESTRATEGIO!! ")
corri = int(input("Ingrese el corrimiento para los mensajes: "))
for x in oficiales:
    palabra = input(f"Ingrese un mensaje para el OFICIAL {x}: ")
    mensaje = ""
    for i in palabra.lower():
        if i in abecedario:
            indice = abecedario.find(i)
            indice_x = (indice+corri)%27
            mensaje += abecedario[indice_x]
        else:
            mensaje += i

    print(f"MENSAJE PARA EL OFICIAL {x}: {mensaje}")
    print("")

#EJERCICIO 2: 

numero = int(input("Ingrese un numero(Para salir ingrese 0): "))
impares = 0
pares = 0


while numero != 0:
    for i in range(len(str(numero))):
        digito = int((numero % (10**(i+1)))/10**i)
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
    numero = int(input("Ingrese un numero(Para salir ingrese 0): "))
    
print(f"Se ingresaron {pares} digitos PARES")
print(f"Se ingresaron {impares} digitos IMPARES")