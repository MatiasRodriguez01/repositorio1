from vehiculo import vehiculo

class coche(vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def mostrar(self):
        print("COCHE:")
        super().mostrar()
        print(f"Velocidad: {self.velocidad}km/h.")
        print(f"Cilindrada: {self.cilindrada}cc.")


