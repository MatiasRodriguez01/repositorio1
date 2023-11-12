class persona:

    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__DNI = ""

    # NOMBRE:    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # EDAD:
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    # DNI:
    @property
    def DNI(self):
        return self.__DNI
    
    @DNI.setter
    def DNI(self, DNI):
        self.__DNI = DNI

    def mostrar(self):
        print(f"Mi nombre es: {self.__nombre}.")
        print(f"Tengo {self.__edad} años.")
        print(f"Y mi documento es {self.__DNI}")
    
    
    def mayor_de_edad(self):
        return self.__edad > 18
            
