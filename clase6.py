# 24/8/23                                  PROGRAMACION 1
#           TRABAJO PRACTICO N°2    
#           TEMA: ESTRUCTURAS CONDICIONALES

# 1- Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la
#    consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo
#    si es mayor a 2 años.
print("Ejercicio 1:")
years = int(input("Ingrese el numero de años que tiene la computadora: "))
if (years <= 2):
    print("EL computador es nuevo.")
else:
    print("El computador es viejo")
print("")

# 2- Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
print("Ejercicio 2:")
if (years < 0):
    print("Error!!!, el numero ingresado es negativo.")
print("")

# 3- Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos
#    variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra.
#    Si no es así, imprimir ‘no hay coincidencia’.
print("Ejercicio 3:")
name1 = input("Ingrese el nombre de la primera persona: ")
name2 = input("Ingrese el nombre de la segunda persona: ")
if (name1[0] == name2[0]):
    print("Coincidencia.")
else:
    print("No hay coincidencia.")
print("")

# 4- Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son:
#  candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.

#     *   Según el candidato elegido (A, B o C) se debe imprimir el mensaje: 
#     *   ‘Usted ha votado por el partido [color del candidato elegido].
#     *   Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, 
#     *   ‘Opción errónea.’

print("EMPIEZAN LAS ELECCIONES!!!!!")
print("Ingrese (A) si quiere votar al partido Rojo")
print("Ingrese (B) si quiere votar al partido verde")
print("Ingrese (C) si quiere votar al partido azul")
print("")
vote = input("Ingrese su voto: ")
if (vote.upper() == "A"): 
    print("Usted a votado al partido ROJO")
elif (vote.upper() == "B"):
    print("Usted a votado al partido VERDE")
elif (vote.upper() == "C"):
    print("Usted a votado al partido AZUL")
else:
    print("Opcion erronea!!")
print("")

# 5 - Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
#     Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
#     informarle que no se puede procesar el dato.

letter = input("Ingrese una letra: ")
if (len(letter) > 2):
    print("Lamento informarle que no se puede procesar el dato!")
elif (letter.upper() == "A"):
    print("Es vocal")
elif (letter.upper() == "E"):
    print("Es vocal")
elif (letter.upper() == "I"):
    print("Es vocal")
elif (letter.upper() == "O"):
    print("Es vocal")
elif (letter.upper() == "U"):
    print("Es vocal")
else:
    print("Usted no ha ingresado una vocal!")

# 6- Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto
# debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

year = int(input("Ingrese el año para saber si es biciesto: "))
if(year % 4 == 0) and (year % 100 != 0):
    print("Es biciesto")
elif (year % 100 == 0) and (year % 400 == 0):
    print("Es biciesto")
else:
    print("No es biciesto")

# 7 - Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres
number1 = int(input("Ingrese el numero 1: "))
number2 = int(input("Ingrese el numero 2: "))
number3 = int(input("Ingrese el numero 3: "))

if (number1 < number2): 
    if (number1 < number3):
        print(f"El menor es {number1}")
    else:
        print(f"El menor es {number3}")
elif (number2 < number1):
    if (number2 < number3):
        print(f"El menor es {number2}")
    else:
        print(f"El menor es {number3}")
print("")

# 8 - Escribí un programa que solicite ingresar un nombre de usuario y una contraseña.
#  Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla 
#  “Usuario y contraseña correctos. Puede ingresar a Camelot”. 
#   Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”
user = input("Ingrese el noombre de usuario: ")
password = input("Ingrese la contraseña: ")

if (user == "Gwenevere" and password == "excalibur"):
    print("¡¡Puede ingresar al camelot!!")
else:
    print("Acceso denegado")
print("")

# 9 -Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#   El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
#   posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre
#   y sexo, y muestre por pantalla el grupo que le correspo
test = input("ingrese su nombre: ")
genre = input("ingrese su genero(masculino/femenino): ")
condition1 = (test[0].lower() < "m"  and genre.lower() == "femenino")
condition2 = (test[0].lower() > "nmar"  and genre.lower() == "masculino")
if condition1 or condition2:
    print("Usted corresponde al GRUPO A")
else:
    print("Usted corresponde al GRUPO B")
print("")

# 10 -Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
#     calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa 
#     debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente 
#     es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor
#     de 18 años, $1000.
print("BIENVENIDO A LA SALA DE JUEGOS!!!")
age = int(input("Ingrese su edad para entrar: "))
if (age >= 4 and age <= 18):
    print("Para entrar necesita pagar $500")
elif (age > 18):
    print("Para entrar necesita pagar $1000")
else:
    print("Puede entrar gratis!!")
print("")

# 11- La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes
#     para cada tipo de pizza aparecen a continuación.
#       *   Ingredientes vegetarianos: Pimiento y tofu.
#       *   Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#   Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
#   respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un
#   ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar
#   por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print("Bienvenido a la Pizzeria Bella Napoli!!")
orden = input("Desea una pizza vegetaliana <<si/no>>: ")
if (orden.lower() == "si" ):
    print("INGREDIENTES VEGETARIANOS:")
    optionA = " con pimiento y tofu."
    optionB = " solo con pimiento."
    optionC = " solo con tofu."
    print(f"A){optionA}")
    print(f"B){optionB}")
    print(f"C){optionC}")
    print(f"D) sin ingredientes.")
    options = input("Ingrese una de las opciones: ")
    if (options.lower() == "a"):
        print(f"Ordeno una pizza de mozzarella{optionA}")
    elif (options.lower() == "b"):
        print(f"Ordeno una pizza de mozzarella{optionB}")
    elif (options.lower() == "c"):
        print(f"Ordeno una pizza de mozzarella{optionC}")
    else:
        print(f"Ordeno pizza de mozzarella")
else:
    print("INGREDIENTES NO VEGETARIANOS:")
    optionA = " con peperoni, jamon y salmon,"
    optionB = " con peperoni y jamon."
    optionC = " con peperoni y salmon."
    optionD = " con jamon y salmon."
    optionE = " con peperoni."
    optionF = " con jamon."
    optionG = " con salmon"
    print(f"A){optionA}")
    print(f"B){optionB}")
    print(f"C){optionC}")
    print(f"D){optionD}")
    print(f"E){optionE}")
    print(f"F){optionF}")
    print(f"G){optionG}")
    print("H) sin nada")

    options = input("Ingrese una de las opciones: ")
    if (options.lower() == "a"):
        print(f"Ordeno una pizza de mozzarella{optionA}")
    elif (options.lower() == "b"):
        print(f"Ordeno una pizza de mozzarella{optionB}")
    elif (options.lower() == "c"):
        print(f"Ordeno una pizza de mozzarella{optionC}")
    elif (options.lower() == "d"):
        print(f"Ordeno una pizza de mozzarella{optionD}")
    elif (options.lower() == "e"):
        print(f"Ordeno una pizza de mozzarella{optionE}")
    elif (options.lower() == "f"):
        print(f"Ordeno una pizza de mozzarella{optionF}")
    elif (options.lower() == "g"):
        print(f"Ordeno una pizza de mozzarella{optionG}")
    else:
        print("Ordeno una pizza de mozzarella")


# 12 - Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han 
#   pasado desde ese año o cuántos años faltan para llegar a ese año

year1 = int(input("Ingrese el año actual: "))
year2 = int(input("Ingrese el año cualquiera: "))
if (year1 < year2 ):
    account = (year2 - year1)
    print(f"Faltan {account} años para llegar al año {year2}")
else:
    account = (year1 - year2)
    print(f"Han pasado {account} años desde el año {year2}")
print("")

# 13 - Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
#   Haciendo que el programa avise cuando se escriben valores negativos o nulos.ion 

number1 = int(input("Ingrese el numero 1: "))
number2 = int(input("Ingrese el numero 2: "))
if (number1 < 0 or number1 == 0) or (number2 < 0 or number2 == 0):
    print("Uno de los numero es negativo o nulo")
elif (number1 > number2):
    if (number1 % number2 == 0):
        print(f"El numero {number1} es multiplo del numero {number2}")
else:
    if (number2 % number1 == 0):
        print(f"El numero {number2} es multiplo del numero {number1}")
print("")

# 14 - Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
#   Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos
#   los números sean solución. Se recuerda que la fórmula de las soluciones es 
#   x = -b / a

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
if a == 0 and b == 0:
    print("Todos los números son solución.")
elif a == 0 and b != 0:
    print("La ecuación no tiene solución.")
else:
    x = -b / a
    print(f"La solución es x = {x}")

# 15 - Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. 
#   Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que 
#   pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un
#   círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

print("Quiere calcular el area del triagulo o del circulo:")
print("Ingrese (t o T) para calcular el area del triangulo")
print("Ingrese (c o C) para calcular el area del circulo")
opcion = input("Ingrese su opcion: ")

if (opcion == "t" or opcion == "T"):
    base = int(input("Ingrese la base: "))
    altu = int(input("Ingrese la altura: "))
    area = (base * altu)/2
    print(f"El area del triangulo es {area}")
elif (opcion == "c" or opcion == "C"):
    pi = 3.1416
    radio = int(input("Ingrese el radio del circulo: "))
    area = (pi * radio**2)
    print(f"El area del circulo es {area}")
print("")

# 16 - Haz una calculadora básica pida al usuario dos valores, a y b.
#       Según la opción que desean, realizar la operación:
#       *   Si operación es 1 entonces debemos ver el resultado de a + b
#       *   Si operación es 2 entonces debemos ver el resultado de a * b
#       *   Si operación es 3 entonces debemos ver el resultado de a - b
#       *   Si operación es 4 entonces debemos ver el resultado de a / b

a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
print("Ingrese una de las siguientes opciones:")
print("Ingrese (1) para Sumar los numeros")
print("Ingrese (2) para restar los numeros")
print("Ingrese (3) para multiplicar los numeros")
print("Ingrese (4) para dividir los numeros")

option = int(input("Ingrese una de las opciones: "))
if (option == 1):
    print(f"Suma = {a+b}")
elif (option == 2):
    print(f"Resta = {a-b}")
elif (option == 3):
    print(f"Multiplicacion = {a*b}")
elif (option == 4):
    print(f"Division = {a/b}")
else:
    print("La opcion ingresada no es correcta!!")

# 17 - Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
#   otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el
#   día ingresado no es ninguno de esos, imprimir otro mensaje

day = input("Ingrese un dia de la semana: ")
if (day.lower() == "lunes"):
    print(f"Es {day.lower()}")
elif (day.lower() == "martes"):
    print(f"Es {day.lower()}")
elif (day.lower() == "miercoles"):
    print(f"Es {day.lower()}")
elif (day.lower() == "jueves"):
    print(f"Es {day.lower()}")
elif (day.lower() == "viernes"):
    print(f"Es {day.lower()}")
elif (day.lower() == "sabado"):
    print(f"Es {day.lower()}") 
elif (day.lower() == "domingo"):
    print(f"Es {day.lower()}")
else:
    print("El valor ingresado no es correcto!!")
print("")


# 18 - Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#   La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas
#   extras y mostrar esta cantidad.
#   Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las 
#   horas laborales comunes.

hourly_wage = int(input("Ingrese su sueldo por hora: "))
hours = int(input("Ingrese las horas trabajadas: "))
overtime = hourly_wage *0.10

if (hours <= 48):
    sueldo = hourly_wage * hours
    print(f"Su sueldo total es de ${sueldo}.")
else:
    sueldo = hourly_wage *  hours
    overtime = sueldo * 0.10
    print(f"Su sueldo total es de ${sueldo+overtime}.")
print("")

# 19 - Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más,
#    existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario
#    no hay descuento.

pens = int(input("Ingrese la cantidad de lapices que quiere comprar: "))
if pens >= 1000:
    discount = (pens * 60)*0.7 
    print(f"El monto total de la compra es ${(pens*60)+discount}")
    print("Con un descuento del 7%")
else:
    print(f"El monto total de la compra es de ${pens*60}/sin descuento")

# 20 - Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de 
#     cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.

print("Ingrese sus 4 notas para saber su promerdio")
note1 = int(input("Ingrese la nota 1: "))
note2 = int(input("Ingrese la nota 2: "))
note3 = int(input("Ingrese la nota 3: "))
note4 = int(input("Ingrese la nota 4: "))
average = (note1+note2+note3+note4)/4
if (average >= 6):
    print(F"Usted aprobo con un promedio de {average}")
else:
    print(F"Usted desaprobo con un promedio de {average}")