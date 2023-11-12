from Perro import Perro
from Gato import Gato
from Pajaro import Pajaro
from Hamster import Hamster

mi_perro = Perro("Atenea", 8, "Hembra", "Dogo Argentino")
mi_gato = Gato("Catalina", 4, "Hembra", "Anaranjado")
mi_pajaro = Pajaro("Juan", 7, "Macho", "Canario")
mi_hamster = Hamster("Teodoro", 1, "Macho", "Anaranjado y Negro")

print("---Informacion del Perro---")
mi_perro.informacion()
mi_perro.hacer_sonido()

print(" ")
print("---Informacion del Gato---")
mi_gato.informacion()
mi_gato.hacer_sonido()

print(" ")
print("---Informacion del Pajaro---")
mi_pajaro.informacion()
mi_pajaro.hacer_sonido()

print(" ")
print("---Informacion del Hamster---")
mi_hamster.informacion()
mi_hamster.hacer_sonido()