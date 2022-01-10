import pandas as pd
import numpy as np


def comRut(i):
        if len(str(i)) == 8:
            i = '00' + str(i)
            return(i)
        else:
            i = '0' + str(i)
            return(i)


df = pd.read_csv('entrada/archivo.csv')
dfPrint = pd.DataFrame()
dfWhere = pd.DataFrame()
numpy_array = df.to_numpy()
array = np.array(df)

print(df.head())  # Imprime muestra datos

script = input("Ingrese nombre script: ")
num_cols = int(input("Ingrese numero de columnas a utilizar: "))

lst = []
lst2 = []
lstw = []
toPrint = []


for i in range(0, num_cols):
    ele = input(f"Ingrese columnas: {i} ")
    lst.append(ele)

print(lst)
argumento0 = input("Ingrese sentencia:\n")
df.insert(0, "Texto", argumento0)  # Add columns

num_cols_w = int(input("Ingrese numero de columnas a utilizar en where: "))

for i in range(0, num_cols_w):
    ele = input(f"Ingrese columnas where: {i} ")
    lstw.append(ele)

print(lstw)

for x in df['rut']:
    lst2.append(comRut(x))

n = df.columns[1]                       # Para Rut
df.drop(n, axis=1, inplace=True)        # Para Rut
df.insert(1, "Rut", lst2)               # Para Rut

for i in range(len(lst)):
    df[lst[i]] = [lst[i]+"='"+str(x)+"'," for x in df[lst[i]]]  # Insert text

for i in df[lst]:
    dfPrint[i] = df[i].values


dfPrint.insert(0, "Texto", argumento0)
dfPrint['where'] = 'where'

for i in df[lstw]:
    dfWhere[i] = df[i].values
# dfPrint[i] = df[i].values

dfWhere = dfWhere.add_suffix('_X')

# dfPass = dfWhere
dfPrint = dfPrint.join(dfWhere)

# print(dfWhere)

dfPrint[dfPrint.columns[-3]] = dfPrint[dfPrint.columns[-3]].str.replace(r',', '')
dfPrint[dfPrint.columns[-2]] = dfPrint[dfPrint.columns[-2]].str.replace(r',', '')
dfPrint[dfPrint.columns[-1]] = dfPrint[dfPrint.columns[-1]].str.replace(r',', ';')

print(dfPrint)
# print(df.head())

np.savetxt(script, dfPrint, fmt="%s")


# def addMisc(): # Add like '=' or "''"
