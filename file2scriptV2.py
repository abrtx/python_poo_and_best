import pandas as pd
import numpy as np
import re
import sys

class Input:

    num_entrada = 0
    num_salida = 0

    def __init__(self): #
        self.ruta = "entrada/"
        self.lst = []
        self.lstW = []
        
        Input.num_entrada += 1
        Input.num_salida += 1

    def data_input(self):
        return input('Please enter file name: ')

    def sentence_input(self):
        return input('Please enter sentence: ')

    def path_to_file(self, entrada):
        return f'{self.ruta}' + entrada

    def add_columns(self):
        cols = input('Please add columns: ')
        list = cols.split(',')
        self.lst.extend(list)

    def add_columns_w(self):
        cols = input('Please add columns where: ')
        list = cols.split(',')
        self.lstW.extend(list)


    def construye(self,df,sentence,ddlordml):
        df2 = pd.DataFrame()

        if ddlordml == 'u':
            In.add_columns()
            for i in range(len(self.lst)):
                df2[self.lst[i]] = [self.lst[i]+"='"+str(x)+"'," for x in df[self.lst[i]]]  

            df2.insert(0, "Texto", sentence)
            df2[df2.columns[-1]] = df2[df2.columns[-1]].str.replace(r',', '')

            In.add_columns_w()
            df_W = In.add_where(df)
            df2 = df2.join(df_W)

        else:
            In.add_columns()
            for i in range(len(self.lst)):
                df2[self.lst[i]] = ["'"+str(x)+"'," for x in df[self.lst[i]]]

            df2.insert(0, "Texto", sentence)
            if self.lst[-1]:
                df2[self.lst[i]]=["'"+str(x)+"');" for x in df[self.lst[i]]]
        return df2

    def add_where(self,df):
        dfW = pd.DataFrame()
        for i in range(len(self.lstW)):
            dfW[self.lstW[i]] = [self.lstW[i]+"='"+str(x)+"'," for x in df[self.lstW[i]]]  
            dfW = dfW.add_suffix('_X')
            dfW.insert(0, "where", "where")
            dfW[dfW.columns[-1]] = dfW[dfW.columns[-1]].str.replace(r',', ';')
        return dfW

    def dml_ddl(self,sentence):
        sentence = sentence.lower()
        if re.search('^update',sentence):
            return 'u'
        elif re.search('^insert', sentence):
            return 'i'
        else:
            print('Ingrese sentencia valida!')
            sys.exit()
    
        
if __name__ == "__main__":
    In = Input()
    di = In.data_input()
    dipluspath = In.path_to_file(di)
    df = pd.read_csv(dipluspath)
    print(df)

    sentence = In.sentence_input()

    ddlordml = In.dml_ddl(sentence)

    df_c = In.construye(df,sentence,ddlordml)

    print(df_c)

    dipluspath=dipluspath.split(".")
    file=dipluspath[0]+".sql"
    np.savetxt(file, df_c, fmt="%s")

# Agregar funcion para realizar en DB directamente
