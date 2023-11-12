import Fcs_ordenamiento as funciones
import Funciones_tp10 as f


print("EJERCICIO 6:")
array_numbers = f.fill_random_list()
print("Lista original = ", array_numbers)

array_numbers = funciones.count_sort(array_numbers)
print("Lista ordenada(metodo de conteo) = ", array_numbers)