#31/8/23                            PROGRAMACION
#           TEMA = ESTRUCTURA SECUENCIAL
#   EJERCICIOS:

# 1 - Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Ingrese una palabra: ")

for i in range(10):
    print(palabra)
print("")

# 2 - Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
#     que ha cumplido (desde 1 hasta su edad).
edad = int(input("Ingrese su edad: "))

for i in range(1, edad+1):
    print(f"Compleaños {i}")
print("")

# 3 - Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
#    todos los números impares desde 1 hasta ese número separados por comas

num = int(input("Ingrese un numero positivo: "))

for i in range(1, num+1, 1):
    if (i == num):
        if (num % 2 != 0):
            print(i)
    elif (i % 2 != 0):
        print(i, end=", ")
print("")

# 4 - Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la
#    cuenta atrás desde ese número hasta cero separados por comas.
num = int(input("Ingrese un numero positivo: "))

for i in range(num, -1, -1):
    if i == 0:
        print(i)
    else:
        print(i, end=", ")

# 5 - Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
#  número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
invest = int(input("Ingrese la cantidad a invertir: "))
interest = int(input("Ingrese el porcentaje de interes: "))
years = int(input("Ingrese los años a invertir: "))

interest /= 100
amount = 0

for i in range(1, years+1):
    amount = invest*interest
    invest += amount
    print(f"En el año {i} el capital obtenido fue de ${int(invest)}")
print("")

# 6 - Escribir un programa que pida al usuario un número entero y muestre por pantalla
#    un triángulo rectángulo como el de más abajo, de altura el número introducido.

number = int(input("Ingrese un numero positivo: "))

print("")
for i in range(1, number+1):
    print("*" * i)
print("") 

# 7 - Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10

print("TABLAS DE MULTIPLICAR DEL 1 AL 10")
print("")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} X {j} = {i*j}")
print("")

# 8 - Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
#   rectángulo como el de más abajo.

number = int(input("Introduce la altura del triangulo: "))
for i in range(1, number+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

# 9 - Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte
#  al usuario por la contraseña hasta que introduzca la contraseña correcta.

password = input("Introduzca su contraseña: ")
entre = True
while entre:
    if password == "1234":
        print("Acceso concedido")
        entre = False
    else:
        password = input("CONTRASEÑA INCORRECTA!!| Introduzca su contraseña: ")
print("")

# 10 - Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no

number = int(input("Ingrese un numero para saber si es primo o no: "))
cont = 0
for i in range(1,number+1):
    if number % i == 0:
        cont += 1
if cont == 2:
    print(f"El numero {number} es primo")
else:
    print(f"El numero {number} no es primo")
print("")

# 11 - Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras 
# de la palabra introducida empezando por la última.

word = input("Ingrese una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i], end=" ")
print("")

# 12 - Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla
#  el número de veces que aparece la letra en la frase.

word = input("Ingrese una frase cualquiera: ")
letter = input("Ingrese la letra que desea encontrar en la frase: ")
counter = 0
for i in word.lower():
    if letter.lower() == i:
        counter += 1
print(f"La letra {letter} aparece {counter} veces.")
print("")

# 13 - Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario
#  escriba “salir” que terminará

exit = True
print("Ingrese palabras(Ingrese [salir] para salir): ")
while exit:
    palabra = input()
    if (palabra == "salir"):
        exit = False
print("")

# 14 -Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares
#  desde el primero hasta el segundo.

number1 = int(input("Ingrese el numero 1: "))
number2 = int(input("Ingrese el numero 2: "))

for i in range(number1, number2+1):
    if i % 2 == 0:
        print(f"El numero {i} es PAR.")
    else:
        print(f"El numero {i} es IMPAR.")

# 15 - Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

number = int(input("Ingrese un numero: "))
if number > 0:
    for i in range(1, number+1):
        if number % i == 0:
            print(f"{i} es divisor de {number}")
else:
    print("El numero es negativo!!")
print("")

# 16 - Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y
#  escriba cuántos negativos ha introducido.

negatives = 0
quantity = int(input("Ingrese la cantidad de numeros que quiere introducir: "))
for i in range(1, quantity+1):
    number = int(input(end = "Ingrese un numero: "))
    if number < 0:
        negatives += 1
print(f"Se ingresaron {negatives} numeros negativos")
print("")

# 17 -


# 18 - Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
# La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma 
# de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

print("FIBONACCI: ") 
old_number = 0
new_number = 1
for i in range(0,11):
    if (i == 0 or i == 1):
        print(i, end=" ")
    else:
        aux = (old_number + new_number)
        print(aux, end=" ")
        old_number = new_number
        new_number = aux

# 19 - Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, 
#  que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una
#  y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al 
#  objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.

quantity = int(input("Ingrese la cantidad que se propone llegar: "))
savings = 0

while savings <= quantity:
    savings += int(input("Ingrese la cantidad que desee ahorar: "))

print(f"La cantidad obtenida es de ${savings}")
print("")

## 20 - Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar 
# la sumatoria de todos los números ingresados.

numbers = int(input("Ingrese un numero(Ingrese 0 para salir): "))
sum = 0
while numbers != 0:
    sum += numbers
    numbers = int(input("Ingrese un numero(Ingrese 0 para salir): "))

print(f"La suma de todos los numeros ingresados es {sum}")

# 21 - Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál
#  fue el mayor número ingresado.

numbers = int(input("Ingrese un numero(Ingrese 0 para salir): "))
max = 1
while numbers != 0:
    if numbers > max:
        max = numbers
    numbers = int(input("Ingrese un numero(Ingrese 0 para salir): "))
print(f"El numero mayor de los numeros ingresados es {max}")
print("")

# 22 - Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma
#  de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar,
#  mostrar cuántos de los números ingresados por el usuario fueron números pares.

