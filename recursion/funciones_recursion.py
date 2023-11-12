
# EJERCICIO 1:

def laberinto(x):
    if x != 0:
        print(f"La rata tardará {x} minuto en salir.")
        laberinto(x-1)

def caminos_a_elegir(caminos, opciones):
    if caminos == 3:
        print("Ingrese uno de los caminos para salir del laberinto:")
        print(f"{opciones[0]}) camino.")
        print(f"{opciones[1]}) camino.")
        print(f"{opciones[2]}) camino.")
    elif caminos == 2:
        print("Ingrese uno de los caminos para salir del laberinto:")
        print(f"{opciones[0]}) camino.")
        print(f"{opciones[1]}) camino.")
    elif caminos == 1:
        print("Ingrese el caminos para salir del laberinto:")
        print("Solo queda el camino")
        print(f"{opciones[0]}) camino.") 
    return int(input("opcion: "))

def opciones_a_elegir(option, options, minutos):
    if (option == options[0]):
        tiempo = minutos[0]
        options.remove(option)
        minutos.remove(tiempo)
    elif (option == options[1]):
        tiempo = minutos[1]
        options.remove(option)
        minutos.remove(tiempo)
    elif (option == options[2]):
        tiempo = minutos[2]
        options.remove(option)
        minutos.remove(tiempo)
    
    return options, minutos, tiempo

def linea():
    print("----------------")

# EJERCICIO 2

def f(n):
    s = str(n)
    #print(f"s = {s}")
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))