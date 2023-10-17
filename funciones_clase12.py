import math
import random

# EJERCICIO 1
def quality_document(documento):
    return (len(documento) == 7 or len(documento) == 8)


# EJERCICIO 2
def quality_letter(palabra):
    for i in range (len(palabra)-1,-1,-1):
        if palabra[i] == " ":
            palabra += " "
            return len(palabra[i+1:-1])


# EJERCICIO 3
def registro(x):
    name1 = ""
    name2 = ""
    name3 = ""
    x += " "
    for i in range(0,len(x)):
        if (i == 0):
            checkPoint_1 = i
        # Con este else sacamos el apellido y serramos el programa
        elif i == (len(x)-1):
            name3 = x[checkPoint_1+1:i]
            return name1,name2,name3
        
        # Con esta condicion averiguamos si la palabra contiene un espacio en medio
        elif (x[i] == " "):
            # Con esta condicion sacamos el primer nombre
            if checkPoint_1 == 0:
                name1 = x[checkPoint_1:i]
                checkPoint_1 = i
                checkPoint_2 = checkPoint_1
            # con este elif sacamos el segundo nombre
            elif checkPoint_1 == checkPoint_2:
                name2 = x[checkPoint_1+1:i]
                checkPoint_1 = i
            

def id(x1, x2, dni):
    return x1 + (str(len(x2))) + dni[0:3]
            

# EJERCICIO 4
def multiplos(n1, n2):
    return (n1 % n2 == 0)
    
def ingrese_numeros():
    return int(input("Ingrese el numero 1: ")), int(input("Ingrese el numero 2: "))


# EJERCICIO 5
def temp_mediun(temp_max, temp_min):
    return round((temp_max + temp_min)/2, 1)



# EJERCICIO 6
def espace_word(word):
    val = ""     
    for i in word:
        val += i
        val += " "
    return val
   


# EJERCICIO 7
def llenar_lista(lista):
    for i in range(10):
        lista.append(random.randint(0,50))
    return lista


def element_max_and_min(lista):
    val_max = 0
    val_min = 0
    for i in lista:
        if (val_max == 0 and val_min == 0):
            val_max = i
            val_min = i
        elif (i > val_max):
            val_max = i
        elif (i < val_min):
            val_min = i
    return val_min, val_max


# EJERCICIO 8:
def area_perimetro(r):
    area = math.pi * r ** 2
    perimetro = 2 * math.pi * r
    return area, perimetro


# EJERCICIO 9:
def login(usuario, contrasenia):
    if (usuario == "usuario1" and contrasenia == "asdasd"):
        return True
    else:
        return False
    

# EJERCICIO 10:
def aplicar_descuento(carrito):
    total = 0
    for producto in carrito:
        precio = carrito[producto]['precio']
        descuento = carrito[producto]['descuento']
        precio_final = precio - (precio * descuento / 100)
        total += precio_final
    return total


# EJERCICIO 12:
def dicc_word(palabra):
    diccionario = {}
    for i in range(len(palabra)):
        diccionario.setdefault(str(i+1),palabra[i])

    diccionario.setdefault("longitud",len(palabra))
    return diccionario


# EJERCICIO 13:
def module(x1, x2):
    vector = ((x1**2) + (x2**2))**(1/2)
    return round(vector, 2)


# EJERCICIO 14
def primo(numero):
    count = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            count += 1
    return count == 2


# EJERCICIO 15: 
def factorial(number):
    fact = 0
    for i in range(number+1):
        if i == 0 or i == 1:
            auxiliar = 1
        else:
            fact = auxiliar * i
            auxiliar = fact
    return fact


# EJERCICIO 16: 
def encontrar_digito(numero, digito):
    cont = 0
    while numero > 0:
        dig = numero % 10
        if (digito == dig):
            cont += 1
        numero //= 10
    return cont



# EJERCICIO 17:
def sum_digits(numero):
    sum = 0
    dig = 0
    while numero > 0:
        dig = numero % 10
        sum += dig
        numero //= 10
    return sum


def mayor_numero(numero, mayor):
    if (mayor == 0):
        mayor = numero
        return mayor
    elif (numero > mayor):
        mayor = numero
        return mayor
    else:
        return mayor