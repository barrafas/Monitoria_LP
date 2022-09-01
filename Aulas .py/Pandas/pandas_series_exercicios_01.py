import numpy as np
import numpy.random as npr
import pandas as pd

#Escreva um programa para somar, subtrair, multiplicar e dividir os elementos de duas séries
serie_1 = pd.Series([2, 4, 6, 8, 10])
serie_2 = pd.Series([1, 3, 5, 7, 9])
serie_3 = serie_1 + serie_2
print("Soma: ")
print(serie_3)
print("Subtração: ")
serie_3 = serie_1 - serie_2
print(serie_3)
print("Multiplicação: ")
serie_3 = serie_1 * serie_2
print(serie_3)
print("Divisão: ")
serie_3 = serie_1 / serie_2
print(serie_3)

#Escreva um programa para calcular a média e o desvio padrão de uma série
print("Média: ", serie_3.mean())
print("Desvio Padrão: ", serie_3.std())

#Escreva um programa para contar a frequência de valores em uma série
serie_numeros = pd.Series(np.random.randint(10, size=42), np.arange(42))
print("Série: \n", serie_numeros, sep="")
print("Frequência: \n", serie_numeros.value_counts(), sep="")
print("Frequência Ordenada: \n", serie_numeros.value_counts().sort_values(), sep="") #Ordenação por elemento... índices são embaralhados

#Escreva um programa para encontrar a posição dos elementos múltiplos de 5
resultado = np.where(serie_numeros%5 == 0)
print("Índices dos múltiplos de 5: \n", resultado, sep="")

#Escreva um programa que encontra os elementos de uma série que não pertencem à outra série
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
print("Série 1: \n")
print(sr1)
print("\nSérie 2: \n")
print(sr2)
print("\nItens da série 1 que não estão presentes na série 2: ")
print("Passo 1: \n", sr1.isin(sr2), sep="")
print("\nPasso 2: \n", ~sr1.isin(sr2), sep="")
print("\nPasso 3: \n", sr1[~sr1.isin(sr2)], sep="")

#Escreva um programa que encontra as posições dos elementos de uma série em uma outra série
sr1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 42])
sr2 = pd.Series([7, 42, 100])
resultado = []

for elemento in sr2:
    try:
        index = pd.Index(sr1).get_loc(elemento)
    except KeyError as error:
        print("Item não encontrado")
    else:
        resultado.append(index)

resultado = pd.Series(resultado)
print("Posição dos elementos da série 2 na série 1: \n", resultado, sep="")

#Escreva um programa que substitui todos os elementos em uma série - exceto os mais frequentes - por "Desconsiderar"
#Para casa: resolver utilizando "unique"
np.random.seed(42)
serie = pd.Series(np.random.randint(1, 10, 42))
print("Série: \n", serie, sep="")
frequencias = serie.value_counts()
print("Frequências: \n", frequencias, sep="")

#passo_1 = serie.value_counts().index[:1]
passo_1 = serie.value_counts().index[0]
passo_1 = pd.Series(passo_1)
print("Passo 1: ", passo_1)

passo_2 = serie.isin(passo_1)
print("Passo 2: ", passo_2)

passo_3 = ~passo_2
print("Passo 3: ", passo_3)

serie[passo_3] = "Desconsiderar"
print("Último passo: \n", serie, sep="")

#Escreva um programa que avalia duas séries e exibe todos os elementos que estão presentes em apenas uma das séries
serie_1 = pd.Series([1, 2, 3, 4, 5])
serie_2 = pd.Series([4, 5, 6, 7, 8])
print("Série 1: \n", serie_1, sep="")
print("Série 2: \n", serie_2, sep="")

serie_uniao = pd.Series(np.union1d(serie_1, serie_2))
print("Série União: \n", serie_uniao, sep="")

serie_intersecao = pd.Series(np.intersect1d(serie_1, serie_2))
print("Série Interseção: \n", serie_intersecao, sep="")

passo_1 = serie_uniao.isin(serie_intersecao)
print("Passo 1: ", passo_1)

passo_2 = ~passo_1
print("Passo 2: ", passo_2)

print("\nResultado: \n", serie_uniao[passo_2], sep="")