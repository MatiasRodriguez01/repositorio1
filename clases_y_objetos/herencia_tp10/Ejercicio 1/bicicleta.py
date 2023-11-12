from vehiculo import vehiculo

class bicicleta(vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def mostrar(self):
        print("BICICLETA: ")
        super().mostrar()
        print(f"Tipo: {self.tipo}")
