import funciones_trabajoPractico9 as f

print("EJERCICIO 8:")
line = int(input("Ingrese el numero de fila: "))  
column = int(input("Ingrese el numero de columna: "))

result = f.pascal(line, column)
print(f"El valor en la fila {line} y columna {column} del Triángulo de Pascal es: {result}")