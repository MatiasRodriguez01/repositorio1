import funciones_trabajoPractico9 as f
import funciones_clase14 as f2

print("EJERCICIO 5:")
list_numbers = f2.fill_random_list()
print("Dada esta lista =",list_numbers)
number_max = list_numbers[0]
print("El numero mas grande es ", f.element_max_list(list_numbers, number_max, len(list_numbers)))