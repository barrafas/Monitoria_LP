import numpy as np
import pandas as pd

# Exercício
# Banda preferida + 3 Músicas da banda
# TOP 3 Artists EMAp com votação (Strip, UPPER)
# Quantas bandas foram indicadas?
# TOP 3 Songs EMAp com votação (Strip, UPPER)
# Quantas músicas foram indicadas?
# Estatísticas do Tamanho dos Nomes dos Artistas e das Músicas

print("############ CRIAÇÃO ############")
indices = ["Anime 1", "Anime 2", "Anime 3", "Anime 4"]
colunas = ["Nota", "Temporadas", "Episódios", "Comentários"]
dados = [[5, 5, 120, "A"], [5, 3, 39, "B"], [8, 12, 180, "C"], [0, 1, 8, "D"]]
df = pd.DataFrame(dados,index=indices,columns=colunas)
print("DataFrame\n", df, sep="")

# Multi-Index and Index Hierarchy
print("\n\n############ MULTI-INDEX ############")
plataforma = ["CrunchyRoll", "CrunchyRoll", "NetFlix", "NetFlix"]
lancamento = [2020, 2021, 2020, 2021]
indices = pd.MultiIndex.from_arrays([plataforma, lancamento], names=("Plataforma", "Lançamento"))
print("\nÍndices:\n", indices, sep="")

df.reset_index(inplace=True)
df.rename(columns = {"index":"Nome"}, inplace = True)
df.set_index(indices, inplace=True)
print("DataFrame\n", df, sep="")

print("\n\n############ AGRUPAMENTO ############")

print("\nAgrupamento por Plataforma: \n", df.groupby("Plataforma"), sep="") #Reparar o tipo de objeto

print("\n\nAgrupamento por Plataforma: MIN\n", df.groupby("Plataforma").min(), sep="")
print("\n\nAgrupamento por Plataforma: MAX\n", df.groupby("Plataforma").max(), sep="")
print("\n\nAgrupamento por Plataforma: STD\n", df.groupby("Plataforma").std(), sep="")

print("\n\nAgrupamento por Plataforma - Temporadas: STD\n", df.groupby("Plataforma")["Temporadas"].std(), sep="")
print("\n\nAgrupamento por Plataforma - Temporadas - NetFlix: STD\n", df.groupby("Plataforma")["Temporadas"].std(), sep="")

print("\n\n############ CONCATENAÇÃO ############")
# Exemplos de DataFrames
# Como saber que o Tio Rafa copiou o código?
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

print("\nDF1:\n", df1, sep="")
print("\nDF2:\n", df2, sep="")
print("\nDF3:\n", df3, sep="")

# Operações de Concatenação nos dois eixos
print("\nConcatenação em Linha:\n", pd.concat([df1,df2,df3]), sep="")
print("\nConcatenação em Coluna:\n", pd.concat([df1,df2,df3], axis=1), sep="")

print("\n\n############ MERGE -> COLUMN ############")

df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
   
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})    

print("\nDF1:\n", df1, sep="")
print("\nDF2:\n", df2, sep="")

print("\nMERGE em KEY\n", pd.merge(df1, df2, how="inner",on="key"), sep="")

df1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                    'key2': ['K0', 'K1', 'K0', 'K1'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
    
df2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                    'key2': ['K0', 'K0', 'K0', 'K0'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

print("\nDF1:\n", df1, sep="")
print("\nDF2:\n", df2, sep="")

print("\nMERGE em KEY1 e KEY2\n", pd.merge(df1, df2, on=["key1", "key2"]), sep="")

print("\n\n############ JOIN -> INDEX ############")

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2']) 

df2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                    index=['K0', 'K2', 'K3'])

print("\nDF1:\n", df1, sep="")
print("\nDF2:\n", df2, sep="")

print("\nJOIN - LEFT:\n", df1.join(df2), sep="")
print("\nJOIN - OUTER:\n", df1.join(df2, how="outer"), sep="")