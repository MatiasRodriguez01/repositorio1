import random

def fill_matrix_automatically(x):
    matrix = []
    for rows in range(x):
        list = []
        for columns in range(x):
            number = random.randint(1,99)
            list.append(number)
        matrix.append(list)
    return matrix

def fill_matrix_manually(x):
    matrix = []
    for rows in range(x):
        list = []
        for columns in range(x):
            number = int(input(f"Ingrese el valor de la fila {rows+1}: "))
            list.append(number)
        matrix.append(list)
    return matrix

def fill_matrix(size):
    while True:
        option = int(input("Desea agrgar los numeros de la matriz: 1) manualmente, 2) automatica: "))
        print("----")
        matriz = []
        if option == 1:
            matriz = fill_matrix_manually(size)
            return matriz
        elif option == 2:
            matriz = fill_matrix_automatically(size)
            return matriz
        else:
            continue

def fill_diagonally(matrix, size):
    list = []
    for rows in range(size):
        for columns in range(size):
            if (rows == columns):
                number = matrix[rows][columns]
                list.append(number)
    return list

def average_diagonally(list):
    sum = 0
    counter = 0
    for elements in list:
        sum += elements
        counter += 1
    return round(sum/counter)

def average_in_matrix(average, matrix, size):
    for rows in range(size):
        for columns in range(size):
            if average == matrix[rows][columns]:
                return True, rows, columns
    return False, 0, 0

def show_matrix(matrix):
    for rows in matrix:
        print(rows)
    