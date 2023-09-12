#   5/9/2023                                PROGRAMACION
#   TEMA: BREAK Y CONTINUE

# Ejercicio 1:
# * The initial value of the variable x will be 0
# num = 0

# * The increment value will be 1
# num += 1

# * The exit condition of the loop will be greater than or equal to 30
# if num <= 30

# * The execution must be broken when x is equal to 15
# if num == 15

# * You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
# "El valor del bucle es ",+num

# * You must skip the executions with the value of x in 4, 6 and 10
# if num == 4 o num == 6 o num == 10: break  "Se salto el valor 4,6,10 de number"

# * At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
# 'Se ha saltado el valor ' + x ' de x'.


# *  When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was 
#   broken when x was ' + x.
# 'La ejecución del bucle se ha interrumpido cuando x era ' + x '.

number = 0
while number <= 30:
    number += 1
    if number == 15:
        print(f"La ejecucion del bucle se ha interumpido cuando x era {number}")
        break
    elif (number == 4 or number == 6 or number == 10):
        print(f"Se ha saltado el valor de {number} de x")
        continue
    else:
        print(number)
print("")
# Ejercicio 2: 

deposit_total = 0
withdrawal_total = 0
money = 0


while True:
    print("Se encuentra en su cuenta bancaria, INGRESE UNA DE LAS SIGUIENTES OPCIONES:")
    print("* D para depositar dinero")
    print("* R para retirar dinero")
    print("* Ingrese [salir] para salir del banco")
    options = input("Ingrese su opcion: ")
    if options.upper() == "D":
        deposit = int(input("Ingrese el monto que desea depositar: "))
        money += deposit 
        deposit_total += deposit
        continue
    elif options.upper() == "R":
        withdrawal = int(input("Ingrese el monto que desea retirar: "))
        money -= withdrawal
        withdrawal_total += withdrawal
        continue
    elif options.lower() == "salir":
        break
    else:
        print("LA OPCION INGRESADA NO ES VALIDA!!")
            
    print("----------------------------------------------------------------------------")

print("")
print(f"El monto final es de ${money}")
print(f"usted a depositado ${deposit_total}")
print(f"usted a retirado ${withdrawal_total}")
print("")

# Ejercicio 3:

prime_numbers = 0
while True:
    numbers = int(input("Ingrese un numero(ingrese 0 para salir): "))
    if numbers == 0:
        break
    else:
        counter = 0
        for i in range(1, numbers+1):
            if numbers % i == 0:
                counter += 1
        if counter == 2:
            prime_numbers += 1
print(f"Se ingresaron {prime_numbers} numeros primos.")
print("")
# Ejercicio 4:

year1 = int(input("Ingrese el años 1: "))
year2 = int(input("Ingrese el años 2: "))

for i in range(year1, year2+1, 1):
    if ((i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)) and (i % 10 == 0):
        print(f"El año {i} es biciesto y multiplo de 10")
    else:
        continue

print("")

# Ejercicio 5:

print("numeros primos del 1 al 20:")
for i in range(1, 21):
    if i % 2 != 0:
        continue
    else:
        print(i)

print("")

# Ejercicio 6: 

list_numbers = []
for i in range(1,101):
    list_numbers.append(i)

number = int(input("Ingrese el numero que desea encontrar: "))
for x in list_numbers:
    if number == x:
        print(f"El numero {x} fue encontrado")
        break
print("")

# Ejercicio 7:

while True:
    option = int(input("Ingrese una de las opciones 1,2,3,[Ingrese 0 para salir]: "))
    if option == 1:
        print("opcion 1")
        continue
    elif option == 2:
        print("opcion 2")
        continue
    elif option == 3:
        print("opcion 3")
        continue
    elif option == 0:
        print("Salir")
        break
print("")

