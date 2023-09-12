

numero = int(input("Ingrese un numero(Para salir ingrese 0): "))
impares = 0
pares = 0


while numero != 0:
    for i in range(len(str(numero))):
        digito = int((numero % (10**(i+1)))/10**i)
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
    numero = int(input("Ingrese un numero(Para salir ingrese 0): "))
    
print(f"Se ingresaron {pares} digitos PARES")
print(f"Se ingresaron {impares} digitos IMPARES")