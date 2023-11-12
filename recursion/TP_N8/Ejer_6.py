import funciones_trabajoPractico9 as f
import funciones_clase14 as f2

print("EJERCICIO 6:")
list_numbers = f2.fill_numbers()
# list_numbers = [1,3,3,7]
print("--------------")
number = int(input("Ingrese la cantidad de veces que se repetiran los numeros: "))
print("--------------")
print("Dada esta lista =", list_numbers)
print("Tendremos esta lista: ")
print(f.replicar(list_numbers, number, []))