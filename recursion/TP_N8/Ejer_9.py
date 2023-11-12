import funciones_trabajoPractico9 as f

print("EJERCICIO 9:")
caracters = ['a', 'b', 'c', 'd', 'e']
k = int(input("Ingrese k: "))
result = []
f.combinations(caracters, k, "", result)

for cadena in result:
    print(cadena)