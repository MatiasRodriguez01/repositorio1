import funciones_trabajoPractico9 as f

print("EJERCICIO 10:")
sheet_number = int(input("Ingrese un numnero para calcular el ancho de la hoja A(n): "))  
width, length = f.sheet_measure(sheet_number)
print(f"Las medidas de la hoja A({sheet_number}) son: Ancho = {width} mm, Largo = {length} mm")