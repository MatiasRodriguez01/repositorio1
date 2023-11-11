from Animal import Animal

class Perro(Animal):

    def __init__(self, nombre, edad, genero, raza):
        super().__init__(nombre, edad, genero)
        self.raza = raza
    
    def hacer_sonido(self):
        print("EL PERRO LADRA!")

    def informacion(self):
        super().mostrar()
        print(f"Raza: {self.raza}.")