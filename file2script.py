import pandas as pd
import numpy as np


class Transforma:

    num_entrada = 0
    num_salida = 0

    def __init__(self, entrada, ruta="entrada/"): #
        self.entrada = entrada
#        self.salida = salida
#        self.tipoEntrada = tipoEntrada
#        self.tipoSalida = tipoSalida
        self.ruta = ruta
        self.lst = [] 
        
        Transforma.num_entrada +=1
        Transforma.num_salida +=1


    def add_sentence():
        return input('Please input the sentence: ')


    def path_to_file(self):
        return f'{self.ruta}{self.entrada}'

    @staticmethod
    def data_input():
        return Transforma(
            input('Please enter file name: '))

    def add_columns():
        return input('Please add columns: ')

    def data_div(cols):
        list=cols.split(',')
        return list
        

class Salida(Transforma):
    def __init__(self, entrada, ruta, tipoSalida):
        super().__init__(entrada,ruta)
        self.tipoSalida=tipoSalida


    def to_db():
        pass

    def to_file(self):
        return f'{self.tipoSalida}{}'


if __name__ == "__main__":
    e0 = Transforma.data_input()
    e0pluspath= Transforma.path_to_file(e0)

    sentence = Transforma.add_sentence()
    
    df = pd.read_csv(e0pluspath)
    df.insert(0, "Texto",sentence)
    
    e1=Transforma.add_columns()
    
    datos=Transforma.data_div(e1)

    lista=[]
    lista.extend(datos)

    t=Transforma.lst
    print(t.lst[0])
    print(lista)
    print(df)
    print(f'Num entradas: {Transforma.num_entrada}, Num salidas: {Transforma.num_salida}')


    """ 
    La clase Transforma, es utilizada para recibir un archivo 
    csv y construye una query a ser ejecutada en alguna DB o 
    simplemante crear un archivo sql

    Parametros
    ==========
        
    (entrada, tipoEntrada, salida, tipoSalida)

    entrada =
    tipoEntrada = 
    salida = 
    tipoSalida =
    """
    
