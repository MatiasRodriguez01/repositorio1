class cuenta:
    def __init__(self):
        self.__titular = ""
        self.__cantidad = 0.0

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def mostrar(self):
        print("Titular de la cuenta:", self.__titular)
        print("Saldo de la cuenta:", self.__cantidad)

    def ingresarDinero(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("Ingreso una cantidad Negativa!!")

    def retirarDinero(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
        


