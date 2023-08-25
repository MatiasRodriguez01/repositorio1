# 1-Calcular el perímetro y área de un rectángulo dada su base y su altura.
base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))
perimetro = (base + altura)*2
area = (base * altura)
print(f"El perimetro del rectangulo es: {perimetro}")
print(f"El area del rectangulo es: {area}")
print("")

# 2- Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
catetoA = int(input("Ingrese el cateto A: "))
catetoB = int(input("Ingrese el cateto B: "))
catetoC = int(input("Ingrese el cateto C: "))
hipotenusa = (catetoA+catetoB+catetoC)
print(f"La hipotenusa del triangulo rectangulo es: {hipotenusa}")
print("")

# 3- Dados dos números, mostrar la suma, resta, división y multiplicación de ambos
n1 = int(input("Ingrese el numero 1: "))
n2 = int(input("Ingrese el numero 2: "))

suma = (n1+n2)
resta = (n1-n2)
divi = float(n1 / n2)
multi = (n1 * n2)

print(f"suma = {suma}")
print(f"resta = {resta}")
print(f"division = {divi}")
print(f"multiplicacion = {multi}")
print("")

# 4- Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius
g_f = int(input("Ingrese los Grados °F: "))
g_c = float((g_f -32)*5/9)
print(f"los Grados °F a °C es: {g_c}")
print("")

# 5- ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

#       a) A = input(nombre, “¿Cuál es tu canción favorita?”)
     
#       b) precio = input(“Precio: “)
#       total = precio + (precio * 0.1)

#       c) edad = int(input(“Edad: “))
#       print(tu edad es, edad)

#       d) edad = int(input(“Edad: “))
#       print(“Veamos si tu edad es 18…”, edad=18)

nombre = "Matias"
A = input(nombre, "¿Cuál es tu canción favorita?")

precio = float(input("Precio: "))
total = precio + (precio * 0.1)

edad = int(input("Edad: "))
print("tu edad es ", edad)

edad = int(input("Edad: "))
print("Vamos si tu edad es 18.... ", edad)
print("")

# 6- Calcular la media de tres números pedidos por teclado
n1 = int(input("Ingrese el numero 1: "))
n2 = int(input("Ingrese el numero 2: "))
n3 = int(input("Ingrese el numero 3: "))

media = (n1+n2+n3)/3
print(f"la media de los 3 numeros es: {media}.")
print("")

# 7- Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas 
#    horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos
minutos = int(input("Ingrese los minutos: "))
h = int(minutos/60)
m = int(minutos%60)
print(f"Son las {h} horas y {m} minutos.")

# 8- Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
#   el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las 
#   tres ventas que realiza en el mes y el total que recibirá en el mes tomando en 
#   cuenta su sueldo base y comisiones
sueldo = int(input("Ingrese su sueldo base: "))
v1 = int(input("Ingrese el monto de la venta 1: "))
v2 = int(input("Ingrese el monto de la venta 2: "))
v3 = int(input("Ingrese el monto de la venta 3: "))
total = (v1+v2+v3)  
comision = int(input("Ingrese el porcentaje de comision: "))
comision /= 100
extra = int((total*comision)*0.10)
print(f"Recibira ${extra} extra por el 10% comicion de ventas")
print(f"Y cobrara un total de ${sueldo+extra}")
print("")

# 9- Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber 
# cuanto deberá pagar finalmente por su compra.
compra = int(input("Ingrese el monto del producto: "))
descuento = compra * 0.15
print(f"Debera pagar ${compra-descuento} por el producto.")
print("")

# 10- Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
#  Dicha calificación se compone de los siguientes porcentajes:
#   * 55% del promedio de sus tres calificaciones parciales.
#   * 30% de la calificación del examen final.
#   * 15% de la calificación de un trabajo final.
parcial1 = int(input("Ingrese la notas del parcial 1: "))
parcial2 = int(input("Ingrese la notas del parcial 2: "))
parcial3 = int(input("Ingrese la notas del parcial 3: "))

promedio = (parcial1+parcial2+parcial3)/3
promedio = round(promedio)

print(f"promedio = {promedio}")
examen_final = int(input("Ingrese la calificacion del examen final: "))
trabajo_final = int(input("Ingrese la calificacion del trabajo final: "))

print(f"La calificacion final = {round(promedio*0.55 + examen_final*0.30 + trabajo_final*0.15)}")
print("")

# 11- Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto
#  de su diferencia, de modo que el resultado sea siempre positivo)
n1 = int(input("Ingrese el numero 1: "))
n2 = int(input("Ingrese el numero 2: "))

print(f"la distancia que hay entre los numero es {abs(n1-n2)}")
print("")

# 12- Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica
numero = int(input("Ingrese un numero: "))
print(f"la raiz cuadrada de {numero} es: {numero ** 1/2}")
print(f"la raiz cubica de {numero} es: {numero ** 1/3}")
print("")

# 13- Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
#     Ejemplo, si se introduce 23 que muestre 32.
numero = int(input("Ingrese un numero: "))
digito1 = str(numero%10)
digito2 = str(numero//10)
print(digito1+digito2)

# 14- Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que
#     intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
aux = 1
print(f"A = {a}")
print(f"B = {b}")
aux = a
a = b; b = aux
print("------")
print(f"A = {a}")
print(f"B = {b}")
print("")

# 15-Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje
#    hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de 
#    llegada a la ciudad B.
segundos = int(input("Ingrese la cantidad de segundos de viaje: "))
hora = int(segundos/60)/60
print(f"Tardara {hora} hs para llegar a la otra ciudad.")
print("")

# 16- Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
nombre = input("Ingrese su nombre: ")
ape1, ape2 = input("Ingrese su primer apellido: "), input("Ingrese su segundo apellido: ")
print(f"{nombre[0]}, {ape1[0]}, {ape2[0]}")
print("")
# 17- Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. 
#     A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.
usuario = input("ingrese su nombre: ")
print(f"Ahora estas en la matrix, {usuario}")
print("")

# 18- Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, 
#     sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a 
#     pagar.
costo = float(input(f"cuanto costo una cena en un restaurante, {usuario}?: "))
monto_final = ((costo)+(costo*0.062)+(costo*0.10))
print(f"El monto final de la cena es ${monto_final}")
print("")

# 19-Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellosmat
#    en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en 
#    formato dd/mm/aaaa.
print("INGRESE SU FECHA DE NACIMIENTO: ")
fecha = input("Ingrese su fecha de naciem(en formato dd/mm/aaaa):")
dd = input("Ingrese el dia: ")
mm = input("Ingrese el mes: ")
aaaa = input("Ingrese el año: ")
print(f"{dd}/{mm}/{aaaa}")
print("")

# 20- Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato
#      DDMMAAA
print("INGRESE SU FECHA DE NACIMIENTO: ")
fecha = input("Ingrese el dia, el mes y el año(En el formato DDMMAA): ")
print(fecha)
# 

# 21- Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto,
#  para saber cuántos tanques de combustible consumirá el viaje entero. Para eso deben
#  ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros)
#  tiene el tanque y cuántos kilómetros en total recorrerán. Hacer un programa que solicite 
#  los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.

litro = int(input("Ingrese la cantidad litro que va a recargar(de 3 a 15lts): "))
klmetros = int(input("Ingrese la cantidad de kilometros que recorrera la moto con 1lt: "))
print("")
print("La motocicleta tiene una capacidad de 15lts de combustible: ")
print(f"Y la motocicleta recorrera {litro*klmetros}kms con {litro}lts de combustible.")
print("")
