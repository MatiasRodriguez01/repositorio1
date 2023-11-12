from Animal import Animal

class Gato(Animal):

    def __init__(self, nombre, edad, genero, color):
        super().__init__(nombre, edad, genero)
        self.color = color
    
    def hacer_sonido(self):
        print("EL GATO MAULLA!")

    def informacion(self):
        super().mostrar()
        print(f"Color: {self.color}.")


