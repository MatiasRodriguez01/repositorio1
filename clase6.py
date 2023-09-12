# 24/8/23                                  PROGRAMACION 1
#           TRABAJO PRACTICO N°2    
#           TEMA: ESTRUCTURAS CONDICIONALES

# 1- Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la
#    consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo
#    si es mayor a 2 años.

anios = int(input("Ingrese el numero de años que tiene la computadora: "))
if (anios <= 2):
    print("EL computador es nuevo.")
else:
    print("El computador es viejo")
print("")

# 2- Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.

if (anios < 0):
    print("Error!!!, el numero ingresado es negativo.")
    print("")

# 3- Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos
#    variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra.
#    Si no es así, imprimir ‘no hay coincidencia’.

nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")
if (nombre1[0] == nombre2[0]):
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
voto = input("Ingrese su voto: ")
if (voto.upper() == "A"): 
    print("Usted a votado al partido ROJO")
elif (voto.upper() == "B"):
    print("Usted a votado al partido VERDE")
elif (voto.upper() == "C"):
    print("Usted a votado al partido AZUL")
else:
    print("Opcion erronea!!")
print("")

# 5 - Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
#     Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
#     informarle que no se puede procesar el dato.

letra = input("Ingrese una letra: ")
if (len(letra) > 2):
    print("Lamento informarle que no se puede procesar el dato!")
elif (letra.upper() == "A"):
    print("Es vocal")
elif (letra.upper() == "E"):
    print("Es vocal")
elif (letra.upper() == "I"):
    print("Es vocal")
elif (letra.upper() == "O"):
    print("Es vocal")
elif (letra.upper() == "U"):
    print("Es vocal")
else:
    print("Usted no ha ingresado una vocal!")

# 6- Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto
# debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

anio = int(input("Ingrese el año para saber si es biciesto: "))
if(anio % 4 == 0) and (anio % 100 != 0):
    print("Es biciesto")
elif (anio % 100 == 0) and (anio % 400 == 0):
    print("Es biciesto")
else:
    print("No es biciesto")

# 7 - Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres
n1 = int(input("Ingrese el numero 1: "))
n2 = int(input("Ingrese el numero 2: "))
n3 = int(input("Ingrese el numero 3: "))

if (n1 < n2): 
    if (n1 < n3):
        print(f"El menor es {n1}")
    else:
        print(f"El menor es {n3}")
elif (n2 < n1):
    if (n2 < n3):
        print(f"El menor es {n2}")
    else:
        print(f"El menor es {n3}")
print("")

# 8 - Escribí un programa que solicite ingresar un nombre de usuario y una contraseña.
#  Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla 
#  “Usuario y contraseña correctos. Puede ingresar a Camelot”. 
#   Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”
usuario = input("Ingrese el noombre de usuario: ")
contra = input("Ingrese la contraseña: ")

if (usuario == "Gwenevere" and contra == "excalibur"):
    print("¡¡Puede ingresar al camelot!!")
else:
    print("Acceso denegado")
print("")

# 9 -Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#   El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
#   posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre
#   y sexo, y muestre por pantalla el grupo que le corresponde.
prueba = input("ingrese su nombre: ")
genero = input("ingrese su genero(masculino/femenino): ")
condicion1 = (prueba[0].lower() < "m"  and genero.lower() == "femenino")
condicion2 = (prueba[0].lower() > "nmar"  and genero.lower() == "masculino")
if condicion1 or condicion2:
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
edad = int(input("Ingrese su edad para entrar: "))
if (edad >= 4 and edad <= 18):
    print("Para entrar necesita pagar $500")
elif (edad > 18):
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
    print("* Pimiento")
    print("* Tofu")
    ingredientes = input("Que ingredientes desea agregar(ingrese <ninguno> si no quiere agregarle): ")
    if (ingredientes.lower() == "ninguno"):
        print("ORDEN: pizza de mozzarella con tomate")
    else:
        print(f"ORDEN: pizza de mozzarella con tomate, {ingredientes}")
else:
    print("INGREDIENTES VEGETARIANOS:")
    print("* Peperoni")
    print("* Jamón")
    print("* Salmón")
    ingredientes = input("Que ingredientes desea agregar(ingrese <ninguno> si no quiere agregarle): ")
    if (ingredientes.lower() == "ninguno"):
        print("ORDEN: pizza de mozzarella con tomate")
    else:
        print(f"ORDEN: pizza de mozzarella con tomate, {ingredientes}")
    print("")

# 12 - Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han 
#   pasado desde ese año o cuántos años faltan para llegar a ese año

a_actual = int(input("Ingrese el año actual: "))
otro = int(input("Ingrese el año cualquiera: "))
if (a_actual < otro ):
    cuenta = (otro - a_actual)
    print(f"Faltan {cuenta} años para llegar al año {otro}")
else:
    cuenta = (a_actual - otro)
    print(f"Han pasado {cuenta} años desde el año {otro}")
print("")

# 13 - Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
#   Haciendo que el programa avise cuando se escriben valores negativos o nulos.ion 

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
if (num1 < 0 or num1 == 0) or (num2 < 0 or num2 == 0):
    print("Uno de los numero es negativo o nulo")
elif (num1 > num2):
    if (num1 % num2 == 0):
        print(f"El numero {num1} es multiplo del numero {num2}")
else:
    if (num2 % num1 == 0):
        print(f"El numero {num2} es multiplo del numero {num1}")
print("")

# 14 - Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
#   Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos
#   los números sean solución. Se recuerda que la fórmula de las soluciones es 
#   x = -b / a



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

opcion = int(input("Ingrese una de las opciones: "))
if (opcion == 1):
    print(f"Suma = {a+b}")
elif (opcion == 2):
    print(f"Resta = {a-b}")
elif (opcion == 3):
    print(f"Multiplicacion = {a*b}")
elif (opcion == 4):
    print(f"Division = {a/b}")
else:
    print("La opcion ingresada no es correcta!!")

# 17 - Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
#   otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el
#   día ingresado no es ninguno de esos, imprimir otro mensaje

dia = input("Ingrese un dia de la semana: ")

if (dia.lower() == "lunes"):
    print(f"Es {dia.lower()}")
elif (dia.lower() == "martes"):
    print(f"Es {dia.lower()}")
elif (dia.lower() == "miercoles"):
    print(f"Es {dia.lower()}")
elif (dia.lower() == "jueves"):
    print(f"Es {dia.lower()}")
elif (dia.lower() == "viernes"):
    print(f"Es {dia.lower()}")
elif (dia.lower() == "sabado"):
    print(f"Es {dia.lower()}") 
elif (dia.lower() == "domingo"):
    print(f"Es {dia.lower()}")
else:
    print("El valor ingresado no es correcto!!")
print("")


# 18 - Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#   La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas
#   extras y mostrar esta cantidad.
#   Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las 
#   horas laborales comunes.

sueldo_x_hora = int(input("Ingrese su sueldo por hora: "))
horas = int(input("Ingrese las horas trabajadas: "))
horasExtras = sueldo_x_hora *0.10

if (horas <= 48):
    sueldo = sueldo_x_hora * horas
    print(f"Su sueldo total es de ${sueldo}.")
else:
    sueldo = sueldo_x_hora *  horas
    horasExtras = sueldo * 0.10
    print(f"Su sueldo total es de ${sueldo+horasExtras}.")
print("")

# 19 - Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más,
#    existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario
#    no hay descuento.


# 20 - Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de 
#     cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.
