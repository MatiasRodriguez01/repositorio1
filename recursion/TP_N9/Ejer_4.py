import funciones_trabajoPractico9 as f

print("EJERCICIO 4:")
number = int(input("Ingrese un numero, para saber si es par o impar: "))
print(f"El numero {number} = {f.par(number)}")
print(f"El anterior ({number-1}) = {f.par(number-1)}")
print(f"El posterior ({number+1}) = {f.par(number+1)}")