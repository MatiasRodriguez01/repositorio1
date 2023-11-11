import random

'''Imprimir carton'''
def show(matriz):
    for i in matriz:
        print(i)

'''Llenar el carton'''

def repetidos(n, list):
    if n in list:
        return False
    else:
        return True


def numero_en_matriz(list, matrix):
    for filas in matrix:
        for elemento in list:
            while True:
                if repetidos(elemento, filas):
                    break
                else:
                    return False
    return True

def llenar_fila():
    x = []
    n = 5
    while n > 0:
        numero_azar = random.randint(1,75)
        if repetidos(numero_azar, x):
            x.append(numero_azar)
            n -= 1
    return x

def llenar():
    matriz = []
    for filas in range(5):
        fila = []
        if filas == 0:
            fila = llenar_fila()
        else:
            while True:
                fila = llenar_fila()
                if numero_en_matriz(fila, matriz):
                    break
                else:
                    fila = []
        matriz.append(fila)
    return matriz