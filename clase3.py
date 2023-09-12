'''
15/8/23                         programacion 1 
'''
#1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1 = int(input("Ingrese el numero 1: "))

#2. No borres la variable número uno y crea una variable llamada "numero2" asignándole un número decimal de tu elección.
numero2 = int(input("Ingrese el numero 2(que sea un decimal): "))

#3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2
suma = (numero1 + numero2)
print(f"suma = {suma}")

#4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para
#   multiplicación y otra para división. Imprime estas variables
resta = (numero2 - numero1)
multi = (numero2 * numero1)
div = (numero2 / numero1)

print(f"resta = {resta}")
print(f"multiplicacion = {multi}")
print(f"Division = {div}")

#5. Crea una variable llamada "nombre" y asígnale tu nombre como valor
nombre = str(input("Ingrese su nombre: "))

#6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el
#   precio de un artículo ficticio
precio = float(input("ingrese el precio del articulo: "))

#7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
#   un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le
#   quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al
#   100% y el valor 0 al 0%.
descuento = 0.60

#8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y
#   almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que
#   aplicar la lógica de matemáticas
precio_final = (precio * descuento)
print(f"precio final = {precio_final}, con un descuento del {descuento*100} % ")
#9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu
#   elección. Qué sea un string
cadena = input("ingrese una frase, o oracion: ")

#10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas
#   a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de
#   Python
longitud = len(cadena)

print(f"longitud = {longitud}")

#11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
#   conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo
#   mismo.

precio_2 = float(input("Ingrese el precio del articulo: "))
print(int(precio_2))

#12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
#   en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
#   espacio entre medio. Puedes usar libremente la forma de concatenación que quieras
apellido = str(input("Ingrese su apellido: "))
nombre_completo = (nombre + " " + apellido)

print(nombre_completo)

#13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10
edad = int(input("Ingrese su edad: "))
edad += 5
print(edad)
edad -= 10
print(edad)

#14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
#   centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3
altura = float(input("Ingrese su altura: "))
altura *= 3
print(altura)
altura /= 5
print(altura)

#15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después
#   transfórmalo todo en minúsculas con algún método o función de Python.
print(nombre_completo.lower())

#16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
#   para que se transforme todo en minúsculas excepto la primera letra
print(nombre_completo.title())


'''
todo mayuscula
print(nombre_completo.upper())
'''

