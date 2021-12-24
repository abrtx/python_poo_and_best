import datetime

class Person:

    raise_amt= 1.04

    def __init__(self, voto, first, last):
        self.voto = voto
        self.first = first
        self.last = last


class Employee(Person):
    def __init__(self, voto, first, last, antiguedad, salary):
        super().__init__(voto, first, last)
        self.antiguedad = antiguedad
        self.salary = salary

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


    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        voto, first, last, antiguedad, salary = emp_str.split('-')
        return cls(voto, first, last, antiguedad, int(salary))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True


    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


emp_str_1 = "si-Renata-Gaudino-8-70_000"
emp_str_2 = "no-Isabel-Gaudino-10-50000"
emp_str_3 = "si-Florencia-Gaudino-9-80000"


new_emp = Employee.from_string(emp_str_1)

my_date = datetime.date(2021,12,25)


e = Employee('','','','5','')

e.first="Flo"

e.fullName = 'Florencia Potilla'

Employee.set_raise_amt(1.05)

print("")
print(e.first)
print(e.last)
print(e.email)
print(e.fullName)
print(f'{e.antiguedad} anios de antiguedad')
print(e)
print("###### New work ######")
print(Employee.raise_amt)
print(e.raise_amt)
print(f'Salario anual: {new_emp.salary}')
print(f'Habilitado para votar: {new_emp.voto}')
print(Employee.is_workday(my_date))
new_emp.apply_raise()
print(f'Salario incrementado 5%: {new_emp.salary}')
