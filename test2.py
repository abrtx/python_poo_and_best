class Person:
    def __init__(self, voto, first, last):
        self.voto = voto
        self.first = first
        self.last = last


class Employee(Person):
    def __init__(self, voto, first, last, antiguedad):
        super().__init__(voto, first, last)
        self.antiguedad = antiguedad

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullName(self):
        return f'{self.first} {self.last}'

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


#    def __repr__(self):
#        return f'Employee({self.first}, {self.last})'

    def __str__(self):
        return f'Employee({self.first}, {self.last}, {self.antiguedad} anios de antiguedad)'


e = Employee('','','','5')

e.first="Flo"

e.fullName = 'Florencia Potilla'

print("")
print(e.first)
print(e.last)
print(e.email)
print(e.fullName)
print(f'{e.antiguedad} anios de antiguedad')
print(e)
