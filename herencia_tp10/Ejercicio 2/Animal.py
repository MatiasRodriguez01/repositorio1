class Animal:

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}.")
        print(f"Edad: {self.edad} Años.")
        print(f"Genero: {self.genero}.")

    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")