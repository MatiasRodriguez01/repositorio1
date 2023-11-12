import bingo_funciones as bingo
import funciones_clase14
import random
import os


# llenar el carton de bingo()


def horizontal(matriz1, matriz2):
    for i in range(5):
        h = 0; x = []
        for j in range(5):
            if (matriz2[i][j] == 'X'):
                x.append(matriz1[i][j])
                h += 1     
        if h == 5:
            print("BINGO")
            print("En la linea horizontal!!")
            return h, x
        
    return 0, []

def vertical(matriz1, matriz2):
    for i in range(5):
        v = 0; x = []
        for j in range(5):
            if (matriz2[j][i]) == 'X':
                
                x.append(matriz1[j][i])
                v += 1
        if v == 5:
            print("BINGO")
            print("En la linea vertical!!")
            return v, x
    
    return 0, []

def diagonal1(matriz1, matriz2):
    d1 = 0
    x = []
    for i in range(5):
        for j in range(5):
            if i == j:
                if (matriz2[i][j] == 'X'):
                    
                    x.append(matriz1[i][j])
                    d1 += 1
    if d1 == 5:
        print("BINGO")
        print("En la linea diagonal!!")
        return d1, x
    else:
        return 0, []

def diagonal2(matriz1, matriz2):
    d2 = 0
    x = []
    for i in range(5):
        for j in range(5):
            if (i+j) == 4:
                if (matriz2[i][j] == 'X'):
                    x.append(matriz1[i][j])
                    d2 += 1
    if d2 == 5:
        print("BINGO")
        print("En la linea diagonal inversa!!")
        return d2, x
    else:
        return 0, []

def x(matriz, num):
    for filas in range(5):
        for columnas in range(5):
            if matriz[filas][columnas] == num:
                matriz[filas][columnas] = 'X'

    
def encontrar_linea(matriz1, matriz2):
    contador = 0; linea = []
    contador, linea = horizontal(matriz1, matriz2)
    if contador == 5:
        return contador, linea
    contador = 0; linea = []
    contador, linea = vertical(matriz1, matriz2)
    if contador == 5:
        return contador, linea
    contador = 0; linea = []
    contador, linea = diagonal1(matriz1, matriz2)
    if contador == 5:
        return contador, linea
    contador = 0; linea = []
    contador, linea = diagonal2(matriz1, matriz2)
    if contador == 5:
        return contador, linea
    print("No se encontro coincidencias")
    return 0, []


tabla = bingo.llenar()
tabla_auxiliar = tabla.copy()
while True:
    n = random.randint(1,75)
    x(tabla_auxiliar, n)
    print("CARTON DEL BINGO:")
    bingo.show(tabla_auxiliar)
    print("------------")
    print(f"El numero del bingo es = {n}")
    numero = 0; linea = []
    numero, linea = encontrar_linea(tabla, tabla_auxiliar)
    if numero == 5:
        print(linea)
        tecla = input("Se termino el juego, pulse cualquier tecla ")
        break
    else:
        tecla = input("Precione cualquier tecla para continuar ")
        os.system('cls')
