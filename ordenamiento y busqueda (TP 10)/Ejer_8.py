import Fcs_ordenamiento as funciones
import Funciones_tp10 as f

print("EJERCICIO 8:")
array = f.fill_random_list()
print("Lista = ", array)

funciones.merge_sort(array)
print("Lista ordenada(metodo merge): ", array)