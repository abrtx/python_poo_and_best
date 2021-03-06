class Animal(object):
    def __init__(self,nombre):
        self.nombre = nombre

    def imprimirNombre(self):
        print("Nombre:",self.nombre)

class Canino(Animal):
    def __init__(self,nombre):
        super(Canino,self).__init__(nombre)
        self.patas = 4
        self.tipo = "Canino"

class Perro(Canino):
    def __init__(self,nombre,raza):
        super(Perro,self).__init__(nombre)
        self.raza = raza

    def imprimirRaza(self):
        print(self.raza)
        print(self.tipo)
        print(self.patas)


p = Perro("Toby", "Golden")
p.imprimirNombre()
p.imprimirRaza()
