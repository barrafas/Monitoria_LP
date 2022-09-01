import numpy as np
import pandas as pd

lista_1 = [1,2,3,4,5]
lista_2 = ["I","II","III","IV","V"]
dicionario_1 = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}
ndarray_1 = np.array(lista_1)

print(lista_1)
print(lista_2)
print(dicionario_1)
print(ndarray_1)
print(":)"*40)

#Buscar no Google: "Pandas Docs Reference Series"
#https://pandas.pydata.org/pandas-docs/stable/reference/series.html
#Evolução de um NDArray, porém unidimensional
ser_1 = pd.Series(lista_1)
print(ser_1) #Reparar índice

ser_1 = pd.Series(lista_2) #Verificar dType object
print(ser_1)  #Reparar índice

ser_1 = pd.Series(data=lista_1, index=lista_2)
ser_1 = pd.Series(lista_1, lista_2) #Lembrar da ordem ou utilizar forma anterior
print(ser_1)

ser_1 = pd.Series(dicionario_1)
print(ser_1)

ser_1 = pd.Series(ndarray_1)
#ser_1 = pd.Series(ndarray_1, lista_2)
print(ser_1)

print("NumPy: ", ndarray_1, type(ndarray_1))
print("NumPy to List: ", ndarray_1.tolist(), type(ndarray_1.tolist()))

print("Series to Numpy: ", ser_1.to_numpy())
print("Series to List: ", ser_1.to_list()) #Mencionar falta de consistência no nome
print(":)"*40)

#Acessando os elementos
print("Acessando Elementos: \n", ser_1[:3])
print("Acessando Elementos: \n", ser_1.head(3))
print("Acessando Elementos: \n", ser_1[-3:])
print("Acessando Elementos: \n", ser_1.tail(3))

#Acessando via label
print("Acessando via label: ", ser_1[0])
#Qualquer label
ser_1 = pd.Series(dicionario_1)
print("Acessando via label: ", ser_1["I"])

#O que estamos fazendo aqui?
print("Série 1 [IdxMax]: ", ser_1.idxmax())
print("Série 1 [IdxMin]: ", ser_1.idxmin())

#Loc
print("Loc: \n", ser_1.loc["I":"IIV"])
print("ILoc: \n", ser_1.iloc[0:3]) #Posições 0, 1 e 2

ser_1 = pd.Series(lista_1)
print("Loc: \n", ser_1.loc[0:3])
print("ILoc: \n", ser_1.iloc[0:3]) #Posições 0, 1 e 2. Um pouco mais difícil de ver, já que os índices são numéricos
print(":)"*40)

#Operações
dicionario_2 = {"I": 10, "II": 42, "III": 7, "V": 1_000_000}
dicionario_3 = {"I": 1, "II": 12, "III": 13, "IV": 0}

ser_2 = pd.Series(dicionario_2)
ser_3 = pd.Series(dicionario_3)

print("Série 2: \n", ser_2)
print("Série 3: \n", ser_3)

result = ser_2.add(ser_3)
print("Série Add: \n", result) #Que louco!

result = ser_2.sub(ser_3)
print("Série Sub: \n", result) #Que louco!

#Append
print("Série: \n", ser_3)
dicionario_4 = {"V": 42}
ser_4 = pd.Series(dicionario_4)
print(ser_4)
print(pd.concat([ser_3, ser_4]))
print(":)"*40)

#Olha só:
print("Série Count: ", result.count()) #Faz sentido? Non-NA/Null
print("Série Size: ", result.size) #Faz sentido?

#################################### Continuar Aqui ####################################

#Resolvendo
result = ser_2.add(ser_3, fill_value=0)
#result = ser_2.add(ser_3, fill_value="0")
#result = ser_2.add(ser_3, fill_value="Oi")
print("Série Add: \n", result)
#Repetindo:
print("Série Count: ", result.count()) #Faz sentido?
print("Série Size: ", result.size) #Faz sentido?
print(":)"*40)

#Drop
result = ser_2.add(ser_3)
result.dropna() #Acontece algo?
#result.dropna(inplace = True)
print("Série Add: \n", result)
print("Série Count: ", result.count()) #Faz sentido?
print("Série Size: ", result.size) #Faz sentido?
print(":)"*40)

#Fill
result = ser_2.add(ser_3)
result.fillna(42)
#result.fillna(42, inplace = True)
print("Série Add: \n", result)
print("Série Count: ", result.count()) #Faz sentido?
print("Série Size: ", result.size) #Faz sentido?
print(":)"*40)