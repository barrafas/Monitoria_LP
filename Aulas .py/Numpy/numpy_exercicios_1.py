import numpy as np

#Criar um array de 42 zeros
np_array = np.zeros(42)
print(np_array)

#Criar um array de 42 uns
np_array = np.ones(42)
print(np_array)

#Criar uma matriz identidade 5x5
np_array = np.eye(3)
print(np_array)

#Criar um array de inteiros de 7 a 42
np_array = np.arange(7, 43)
print(np_array)

#Criar um array de inteiros pares de 7 a 42
np_array = np.arange(8, 43, 2)
print(np_array)

#Gerar um número entre 0 e 1
number = np.random.rand(1)
print(number)

##Gerar um array com uma amostra aleatória de 10 números de uma distribuição normal
number = np.random.randn(10)
print(number)

#Criar um array com dez 42s
np_array = np.ones(10) * 42
print(np_array)

#Criar uma matriz 3x3 com valores entre 1 e 9
np_array = np.arange(1,10).reshape(3,3)
print(np_array)