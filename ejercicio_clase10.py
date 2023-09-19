# Definiciones de funciones

def most(a, b):
    if (a > b):
        return a
    else:
        return b

def least(a, b):
    if (a < b):
        return a
    else:
        return b

# Programa principal

x = int(input("Ingrese un numero: "))
y = int(input("Ingrese otro numero: "))

print(most(x-3, least(x+2, y-5)))