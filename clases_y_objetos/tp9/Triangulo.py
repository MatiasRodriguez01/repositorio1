class triangulo:

    def __init__(self, lado1, lado2, lado3):
        '''
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
        '''
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    '''
    # Lado 1:
    @property
    def lado1(self):
        return self.__lado1
    
    @lado1.setter
    def lado1(self, lado1):
        self.__lado1 = lado1

    # Lado 2:
    @property
    def lado2(self):
        return self.__lado2
    
    @lado2.setter
    def lado2(self, lado2):
        self.__lado2 = lado2

    # Lado 1:
    @property
    def lado3(self):
        return self.__lado3
    
    @lado3.setter
    def lado3(self, lado3):
        self.__lado3 = lado3
    '''

    def lado_mayor(self):
        if (self.lado1 >= self.lado2):
            if (self.lado1 >= self.lado2):
                print("Lado 1.")
            else:
                print("Lado 3")
        elif (self.lado2 >= self.lado3):
            print("Lado 2.")
        else:
            print("Lado 3.")


    def tipo_triangulo(self):
        if (self.lado1 == self.lado2 == self.lado3):
            print("Triangulo equilatero.")
        elif (self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3):
            print("Triangulo isoceles.")
        else:
            print("Triangulo escaleno.")