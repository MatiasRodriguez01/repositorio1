import Fcs_ordenamiento as funciones

def orden_list(array):
    numbers = []
    strings = []
    for i in array:
        if isinstance(i, int):
            numbers.append(i)
        elif isinstance(i, str):
            strings.append(i)
    
    new_list = []
    funciones.bubble_sort(numbers)
    funciones.bubble_sort(strings)
    new_list = numbers + strings
    return new_list

print("EJERCICIO 7:")
array = [1, "hola", 8, "mañana", 5, "alias", "isaias", 2]
print("Lista original: ", array)

array = orden_list(array)
print("Lista ordenada: ", array)
