import funciones_global as funciones




while True:
    size = int(input("Ingrese el tamaño de la matriz(El valor tiene que ser imapar): "))
    if (size % 2 != 0):
        break

matriz = funciones.fill_matrix(size)
print("----")
print("MATRIZ:")
funciones.show_matrix(matriz)

print("----")
print("DIAGONAL PRINCIPAL:")
diagonally = []
diagonally = funciones.fill_diagonally(matriz, size)
print(diagonally)

print("----")
print("PROMEDIO DIAGONAL:")
average = funciones.average_diagonally(diagonally)
print("EL promedio de la diagonal es = ", average)

print("----")
print("PROMEDIO ESTA EN LA MATRIZ?:")
if (funciones.average_in_matrix(average, matriz)):
    print(F"El numero {average} se encuentra en la matriz!.")
else:
    print(F"El numero {average} no se encuentra en la matriz!.")


