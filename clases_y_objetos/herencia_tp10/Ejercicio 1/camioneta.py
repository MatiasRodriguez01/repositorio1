from vehiculo import vehiculo

class camioneta(vehiculo):

    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga

    def mostrar(self):
        print("CAMIONETA: ")
        super().mostrar()
        print(f"Carga: {self.carga}kg.")

    