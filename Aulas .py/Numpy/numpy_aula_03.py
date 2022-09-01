#NymPy - Lesson 3

import numpy as np
import numpy.random as npr

#Modulo Random

a1D = npr.default_rng(42).random((3,3))
print(a1D)
print(np.sort(a1D))
print(np.sort(a1D, axis=None))

#Broadcasting

lista_a = [1,2,3]
lista_b = [1,2,3]
a1d_a = np.array([1, 2, 3, 4])
a1d_b = np.array([0, 1, 2, 3])

##### OPERAÇÕES BÁSICAS #####
#print(lista_a * lista_b)
#print(a1d_a * a1d_b)
#print("#"*40)
#print(lista_a * 3)
#print(a1d_a * 3)
#print("#"*40)
#print(lista_a + 3)
#print(a1d_a + 3)
#print("#"*40)
#print(lista_a - 3)
#print(a1d_a - 3)
#print("#"*40)
#print(lista_a**3)
#print(a1d_a**3)
#print("#"*40)
#print(lista_a / 3)
#print(a1d_a / 3)
#print("#"*40)
#print(a1d_a / 0)
#print(a1d_b / 0)
#print(a1d_a / a1d_b)

#Produtos entre NDArrays
a1d_a = a1d_a.reshape(1,4)
a1d_b = a1d_b.reshape(4,1)
#a1d_b = a1d_b.reshape(2,2) REPARAR NA MENSAGEM
print(a1d_a)
print(a1d_b)
print(a1d_a*a1d_b) #Produto Tensorial

#Se podemos fazer broadcast
ndarray = np.array([1, 2, 3, 4, 5, 6])
indices = ndarray>3

#O que será impresso?
print(indices)
#O que será impresso?
print(ndarray[indices])

indices = (ndarray%2 == 0)

print(indices)
print(ndarray[indices])

ndarray = np.arange(9).reshape(3,3)
indices = np.array([[False, True, False], [True, False, True], [True, True, True]])
print(ndarray)
print(indices)
print(ndarray[indices])

#Exemplo com nota de série ou anime
  
#Notas do público de uam série de TV
nota = np.array([78, 65, 91, 89, 74, 51, 58, 88])
  
#Average 
print("Average: ", np.average(nota))
#Median
print("Median: ", np.median(nota))
#Standard Deviation
print("Standard Deviation: ", np.std(nota))
#Variance
print("Variance: ", np.var(nota))
#Minimum and Maximum
print("Minimum and Maximum: ", np.amin(nota), np.amax(nota))
#Peak to Peak
print("Peak to Peak: ", np.ptp(nota))
#Percentile
print("Percentile [70]: ", np.percentile(nota, 70))

# Exemplo mais complexo
ndarray = npr.standard_normal(6)
print("\nExemplo mais complexo", np.mean(ndarray, where=[True, False, True, False, True, False]))
#Podemos ter resultados diferentes dependendo da precisão
print("Exemplo mais complexo", np.mean(ndarray, dtype=np.float16))
print("Exemplo mais complexo", np.mean(ndarray, dtype=np.float64))

"""
Exercícios:

Elaborar um programa que trata de uma matriz 2xN composta por:
1 - Uma coleção de valores estimados
2 - Uma coleção de valores observados

E 4 funções:
1 - Erro médio absoluto
2 - Erro médio quadrático
3 - Dados gerais da coleção (selecionada de acordo com o parâmetro passado)
4 - Histograma da coleção (selecionada de acordo com o parâmetro passado)

Dicas: setdiff1d e intersect1d
"""