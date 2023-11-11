from vehiculo import vehiculo

class motocicleta(vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def mostrar(self):
        print("MOTOCICLETA:")
        super().mostrar()
        print(f"Velocidad: {self.velocidad}km/h.")
        print(f"Cilindrada: {self.cilindrada}cc.")
