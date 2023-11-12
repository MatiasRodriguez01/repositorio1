import Fcs_ordenamiento as Fun
import Funciones_tp10 as f


print("EJERCICIO 1:")
list_numbers = f.fill_random_list()
print("Lista original = ", list_numbers)

Fun.bubble_sort(list_numbers)
print("Lista ordenada(metodo burbuja) = ", list_numbers)
