class Animal:

    def __init__(self,nombre, patas, tipo):
        self.nombre = nombre
        self.patas = patas
        self.tipo = tipo

x = Animal("Violeta",4,"Perro")

print(x.nombre,x.patas,x.tipo)
