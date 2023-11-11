from Animal import Animal

class Pajaro(Animal):

    def __init__(self, nombre, edad, genero, especie):
        super().__init__(nombre, edad, genero)
        self.especie = especie

    def hacer_sonido(self):
        print("EL PAJARO CANTA")

    def informacion(self):
        super().mostrar()
        print(f"Especie: {self.especie}.")