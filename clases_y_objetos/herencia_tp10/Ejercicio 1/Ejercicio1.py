from coche import coche 
from bicicleta import bicicleta
from motocicleta import motocicleta
from camioneta import camioneta

def catalogar(lista):
    for vehiculos in lista:
        print("-----------")
        vehiculos.mostrar()
    print("-----------")

def vehiculo_ruedas(lista, rueda):
    counter = 0
    for vehiculos in lista:
        if vehiculos.ruedas == rueda:
            counter += 1
    return counter

mi_auto = coche("Azul", 0, 170, 2000)
mi_moto = motocicleta("Roja", 2, 120, 800)
mi_bicicleta = bicicleta("Negra", 2, "Deportiva")
mi_camioneta = camioneta("Blanca", 4, 450)
vehiculos = [mi_auto, mi_moto, mi_bicicleta, mi_camioneta]

catalogar(vehiculos)

for iterador in range(0, 5, 2):
    print(f"Se han encontrado {vehiculo_ruedas(vehiculos, iterador)} vehiculos con {iterador} ruedas.")
