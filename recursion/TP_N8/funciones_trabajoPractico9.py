
# EJERCICIO 1:

def digits(n):
    if n == 0:
        return 0
    else:
        return 1 + digits(n//10)

# EJERCICIO 2:

def potencia(numero, base):
    if numero <= base:
        return base == numero
    else:
        return potencia(numero//base, base)

# EJERCICIO 3:

def posiciones_de(string1, string2, posicion, lista): 
    if posicion == 0: # cuando la posicion este en 0 devolvera la lista
        return lista
    else:    
        # aca creamos la posicion 'i', que es igual a [la cantidad de caracteres de string1 - 1, menos, la posicion - 1]
        p_i = ((len(string1))-1)-(posicion-1)         
        # en string3 decimos que guarde el un string desde la posicion 'i' 
        # hasta la posicion 'i'+ len(string2)
        string3 = string1[(p_i):(p_i+len(string2))]   
        if string3 == string2:      
            # Aca decimos que decimos que compare el string3 y el string2
            # si la condicion cumple guarda la posicion 'i' en la lista
            lista.append(p_i)
        return posiciones_de(string1, string2, posicion-1, lista)   # Aca llamamos a la funcion y decimos que a la posicion le reste 1
 
'''version normal de ejercicio 3:'''
def posiciones(string1, string2):
    x = []
    for i in range(len(string1)):
        text = string1[i:i+len(string2)]
        if text == string2:
            x.append(i)
    return x

# EJERCICIO 4:

def par(n):
    if (n == 0):
        return "ES PAR."
    else:
        return impar(n-1)
      
def impar(n):
    if (n == 0):
        return "ES IMPAR."
    else:
        return par(n-1)

# EJERCICIO 5:

def element_max_list(lista, max, tam):
    if tam > 0:
        if lista[tam-1] > max:
            max = lista[tam-1]
        return element_max_list(lista, max, tam-1)
    else:
        return max

# EJERCICIO 6:

def replicar(lista, n, vacia):
    if n == 0:
        return sorted(vacia)
    else:
        for i in lista:
            vacia.append(i)
        return replicar(lista, n-1, vacia)

# EJERCICIO 7:

def k(n, p):
    if (n == 0):
        return 0
    else:
        return (n*p) + k(n-1, p)

# EJERCICIO 8:
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)
    
# Ejercicio_9
def combinations(c_list, k, actual="", result=[]):
    if k == 0:
        result.append(actual)
        return

    for caracter in c_list:
        combinations(c_list, k - 1, actual + caracter, result)

# Ejercicio_10

def sheet_measure(sheet_n):
    if sheet_n == 0:
        return (841, 1189)  # Hoja A0
    else:
        previous_width, previous_length = sheet_measure(sheet_n - 1)
        new_width = previous_length
        new_length = previous_width / 2
        return (new_width, new_length)