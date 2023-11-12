import Fcs_ordenamiento as funciones

def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        current_value = arr[i]
        position = i
        
        while position > 0 and len(arr[position - 1]) > len(current_value):
            arr[position] = arr[position - 1]
            position -= 1
        
        arr[position] = current_value
    
    
print("EJERCICIO 3:")
list_strings = ["Metallica", "Guns N Roses", "AC DC", "Korn", "La Renga", "No Te Va Gustar", "Soda Esterio", "Airbag"]
print("Lista original:")
print(list_strings)

insertion_sort(list_strings)
print("Lista ordenada(metodo por insercion):")
print(list_strings)