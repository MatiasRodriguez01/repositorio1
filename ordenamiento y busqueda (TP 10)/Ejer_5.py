import Fcs_ordenamiento as funciones
import Funciones_tp10 as f

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
print("EJERCICIO 5:")
list_numbers = f.fill_random_list()
print("Lista original = ", list_numbers)

bubble_sort(list_numbers)
print("Lista ordenada(metodo burbuja) = ", list_numbers)