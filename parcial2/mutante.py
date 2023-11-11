
'''LLENAR EL ADN'''

# con la funcion fill_adn lo que haremos sera que llene un arreglo con 6 palabras, cada 
# palabra devera tener 6 caracteres
def fill_adn():
    list_letter = []  # aca iniciamos una lista vacia
    letters = ['A','C','G','T']     # Aca iniciamos una lista con la letra que deveria tener las palabras
    print("-------")
    print("INGRESE EL ADN INDIVIDUO: ")
    for i in range(6):
        # iniciamos un bucle for que recorra 6 veces, dentro de el, habra un bucle while
        while True:
            print(f"Ingrese la palabra N°{i+1}:")
            #Dentro del while, escribiremos una palabra que contenga 6 letras, y que contenga 
            # solo los caracteres A,G,C o T. Despues de la modificamos la palabra cambiaremos las letras en mayusculas 
            words = input("Ingrese una palabra de 6 caracteres, que contengan A,G,C o T: ")
            words = words.upper()
            #La siguiente condicion dice que si la palabra contiene 6 letras y que si la funcion validate devuelva True
            # Se agregara la palabra a la lista "x" y hara un break, sino el programa pedira otra vez que ingrese otra palabra 
            if (len(words) == 6) and (validate(letters, words)):
                list_letter.append(words)
                break
    print("-------")
    # Al final devolvemos un la lista con las 6 palabras.
    return list_letter

#La funcion recibira una lista con letras y una palabra
def validate(list, word):
    # lo que va a hacer, es que recorra todas a letra de la palabra recibida
    # y evalue si la letra no se encuentra en la lista de letra, asi con cada una de las letra de la palabra     
    # si cumple de que la letra no esta en la lista devolvera False y se saldra de la funcion
    # de lo contrario seguira de largo y al final devolvera True
    for letters in word:
        if letters not in list:
            return False
    return True    
    

# con la funcion show_matriz mostraremos el ADN por pantalla
def show_matriz(x):
    print("ADN:")
    for i in x:
        for letter in range(6):
            print(end= f"[{i[letter]}]")
        print("")


'''VALIDAR DEL ADN'''

#La funcion horizontally recibe la lista con palabra y la letra a encontrar la secuencia
def horizontally(array, element):
    # Tenemos 2 bucles for uno que recorra una por una las palabras, y otra que recorra desde 0 a 5.
    for word in array:
        counter = 0  # se iniciara un contador inicializado en 0.
        for columns in range(6):
            #En el if decimos que si el elemento del string es igual a la letra recibida 
            # que el contador se valla sumando en 1
            if (word[columns] == element):
                counter += 1
                #Si huvo una secuencia en una palabra con la misma letra, diremos que el 
                # contador es mayor o igual a 4 haga un return que devuelva True
                if (counter >= 4):
                    return True
            else:
                #Si la condicion (word[columns] == element) no se cumple es contador se vuelve a inicializar 
                # en 0 y tendra que comenzar devuelta, si es que hay una secuencia de la letra recibida
                counter = 0
    #Si no se encontro una secuencia de letras en todas la palabra devolvera un False la funcion.
    return False



#La funcion vertically recibe el ADN y a letra encontrada.
def vertically(array, element):
    # Tenemos 2 bucles, ambos correran desde 0 a 5.
    for rows in range(6):
        counter = 0     # se iniciara un contador inicializado en 0.
        for columns in range(6):
            #En la matriz recibira en el primer corchete el 2do for con las columnas.
            # y en el primer corchete el 1er bucle for con las filas.
            # Esto va a hacer que recorra todos los elemento de una determinada columna, analizandon una linea vertical
            # por ejemplo m[0][0] -> m[1][0] -> m[2][0] etc.
            # Entonces decimos que el elemento de la matriz es igual a la letra recibida            
            if (array[columns][rows] == element):
                # si es verdadera entonces el contador se sumara en 1
                counter += 1
        # si el contador es mayor o igual a 4 entonces retornara un True y saldra de la funcion.
        # si no cumple la condicion volvera arriba, el contador se inicializara en 0 y volvera a buscar una secuencia
        if (counter >= 4):
            return True
    # Si al final no encuentra un secuencia entonces retornara un False
    return False



# En la funcion diagonally_1 recibira como parametros el ADN y la LETRA
def diagonally_1(array, element):
    counter = 0  # inicializamos una variable counter en 0.
    #Crearemos 2 bucle for, los 2 desde 0 hasta 5.
    for rows in range(6):
        for columns in range(6):
            # Dentro del bucle tenemos un if, que dira si el elemento de la matriz es igual a la letra recibida
            if array[rows][columns] == element:
                #La variable counter, recibira el resultado de la funcion d1.
                counter = d1(array, element, rows, columns)
                #Si la variable counter es mayor o igual 4, la funcion devolvera True y se saldra de la funcion
                if counter >= 4:
                    return True
    # Si la funcion no encuentra una secuencia entonces devolvera False.
    return False


# La funcion d1 recibira el ADN, la letra que se encontro en la funcion diagonally_1
# y se recibira tambien la linea y columna donde se encuetra la letra
def d1(array, element, rows, columns):
    count = 0  # se inicializara la variable count en 0
    # Se crearan 2 bucles for, uno iniciara desde la fila recibira hasta 5
    # y el otro desde la columna recibida hasta 5
    for i in range(rows, 6):
        for j in range(columns, 6):
            # Aca para analizar la diagonal, diremos que si el valor de la filas
            # es igual al valor de la columnas
            if (j==i):
                # aca decimos si el valor de la matriz es igual a la letra recibida
                # Si la condicion se cumple el valor de "X" aumentara en 1
                if array[i][j] == element:
                    count += 1
            else:
                #En caso de que el elemento este en un lugar especial y la secuencia empiece cuando las
                # filas y las columnas no sean iguales, hacemos una resta con las filas y las columnas.
                # Si la resta es igual a 1 entonces empieza la secuencia
                product = i-j
                if product < 0:
                    # con esto hacemos por si la resta es negativa.
                    product *= (-1)
                # Entonces si la resta es igual 1, empieza la secuencia diagonal.
                if product == 1:
                    if array[i][j] == element:
                        count += 1
    # Al final la funcion devolvera el valor de "X" y se asiganara en la variable "counter" de la funcion diagonally_1
    return count



# En la funcion diagonally_2 recibira como parametros el ADN y la LETRA
def diagonally_2(array, element):
    counter = 0 # inicializamos una variable counter en 0.
    #Crearemos 2 bucle for, uno iniciara de 0 a 5, y el otro en 5 a 0 
    for rows in range(6):
        for columns in range(5, -1, -1):
            #Dentro de una determinada linea decimos que arranque desde el ultimo elemento del string 
            # hasta el primero, y comparara si ese elemento es igual a la letra que recibe la funcion            
            if (array[rows][columns] == element):
                #Si la condicion cumple, la variable counter almacenara el resultado de la funcion d2.
                counter = d2(array, element, rows, columns, columns)
                # Si el valor de counter es igual o mayor que 4 devolvera con un return True, 
                # y se saldra de la funcion 
                if counter >= 4:
                    return True
    # Si el programa paso de largo y encontro una cohicidencia con la letra ingresada devolvera False
    return False

#La funcion d2, recibira la el ADN, la letra, la fila y la columna en el cual se encuentra el elemento de la funcion diagonally_2
# y tambien recibira por segunda vez el valor de la columna
def d2(array, element, rows, columns, condition):
    x = 0 # inicializamos la variable x en 0.
    # Aca inicamos 2 bucles for:
    # * uno se inicializara en la desde el valor de la linea recibida hasta 6.
    # * y el otro se inicializara de 0 hasta la columna recibida 
    for i in range(rows, 6):
        for j in range(0, columns+1):
            # en el if, decimos que la suma de i y j (la fila y columna) sea igual que 
            # condition que es el valor que usaremos para recorrer una diagonal inversa
            if i+j == condition:
                # Si la condicion cumple entrara en esta condicion:
                # que dira si ese elemento de la matriz es igual a la letra recibida,
                # y asi vamos viendo todos los elementos de la diagonal inversa.
                # Si cumple entonces se sumara "X", sino no va a ejecutar nada.
                if (array[i][j] == element):
                    x += 1
    # Al final devolvera a variable x, que se almacenara en la variable "counter" de la funcion diagonally_2.
    return x
    

# Con la funcion "the_sequences" recibira como parametros el adn y la letra
def the_sequences(array, element):
    # iniciaremos un contador que se llame "adn" y acumulara las secuencias horizontales,
    #  verticales, y diagonales que puedan contener dicha letra
    adn = 0 
    if (horizontally(array, element)): #Si encontro una linea horizontal, sumara 1
        adn += 1
    if (vertically(array, element)): # si encontro una linea vertical, sumara 1
        adn += 1
    if (diagonally_1(array, element)): # si encontro una secuencia en la linea diagonal, sumara 1
        adn += 1
    if (diagonally_2(array, element)): # si encontro una secuencia en la otra linea diagonal, sumara 1
        adn += 1
    # Al final devolvera el valor final de adn y se almacenara en la variable "sequence" de la funcion is_mutant
    return adn



'''Tenemos la funcion is_mutant que nos dira si el ADN ingresado es mutante'''
def is_mutant(matrix):  
    total = 0  # Ingresamos la variable "total" que contaremos el total de secuencias encontradas en el ADN
    list_letter = []    #Tenemos la lista que no almacenara la letra que se analizaron asi no se repiten
    # creamos 2 bucle for, uno para iterar cada palabra del arreglo, 
    # y otra para contar las letras de cada palabra
    for rows in matrix:
        for columns in range(6):
            letter = rows[columns] #En "letter" almacenamos la letra a comparar
            sequence = the_sequences(matrix, letter)  #En la variable "sequence" guardara el resultado de la funcion "the_sequences"
            #En el if, veremos si "letter" no se encuentra en la lista de letras repetidas(list_letter)
            if letter not in list_letter:
                #Ahora veremos si el valor que tiene "sequence" se mayor a 0
                if sequence > 0:
                    # con este print mostramos cuantas veces se encontro la letra.
                    print(f"El gen {letter} se encontro {sequence} veces!!")
                    #si cumple entonces la letra "letter" se guardara en list_letter para que no
                    # se repita otra vez en la funcion 
                    list_letter.append(letter)
                    total += sequence #y "sequence" se sumara a la variable "total"
                # En caso de que "sequence" no sea mayor a 0 no se ejecutara el codigo y seguira con el programa
    # si el total de secuencias es mayor a 1, devolvera True, sino devolvera False
    return total > 1

adn2 = [
    "ATGCTA",
    "AGTCAT",
    "ACGTAC",
    "ACGTTG",
    "TTTTTT",
    "CCCCCC"
]

adn3 = [
    "ATGCTA",
    "AGTTAT",
    "ACTAAC",
    "ATATCG",
    "TTTCTT",
    "CCCCCC"
]