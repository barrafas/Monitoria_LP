import numpy as np
import numpy.random as npr

#Criação de ndarrays apenas com base em estruturas tradicionais
#Imprimir linha a linha os exemplos a seguir:
a1D = np.zeros(3)
a1D = np.zeros((3, 3))
a1D = np.zeros((3, 3, 3))

a1D = np.ones(3)
a1D = np.ones((3, 3))
a1D = np.ones((3, 3, 3))

a1D = np.arange(10)
a1D = np.arange(0,100,10)
a1D = np.arange(0,100,10, dtype=np.float64)
a1D = np.arange(0,1,0.01)
a1D = np.linspace(0, 100, 5)

print(type(a1D), "\n", a1D, "\n")
print(f"Dados sobre a1D:\nDimensão: {a1D.ndim}\nForma: {a1D.shape}\nTamanho: {a1D.size}\nTipo: {a1D.dtype}")
print("===============================================================")

#Operações em NDArrays

a1D = np.arange(10)
a1D = a1D.reshape(5,2)
a1D = a1D.reshape(3,2) #Erro!!!
a1D = a1D.transpose()

a1D_A = np.arange(20)
a1D_A = a1D_A.reshape(10,2)
a1D = np.vstack((a1D_A, a1D_A)) #Tupla!!!
a1D = np.hstack((a1D_A, a1D_A)) #Tupla!!!

print(type(a1D), "\n", a1D, "\n")
print(f"Dados sobre a1D:\nDimensão: {a1D.ndim}\nForma: {a1D.shape}\nTamanho: {a1D.size}\nTipo: {a1D.dtype}")

a1D = np.arange(10)
print(a1D)
a1D_copy = a1D
print(a1D_copy)

#Eles são o mesmo objeto?
print(id(a1D))
print(id(a1D_copy))

a1D_copy[0] = 42
print(a1D)
print(a1D_copy)

#Funções normalmente retornam cópias dos NDArrays originais
outro_vetor = a1D.reshape(5,2)
outro_vetor[0,0] = 1000
print(outro_vetor)
print(a1D)

#O que está acontecendo? Estas cópias são superficiais 

a1D = np.arange(10)
a1D_copy = a1D.copy() #Deep Copy
print(id(a1D))
print(id(a1D_copy))

print(a1D)
print(a1D_copy)

a1D_copy[0] = 42
print(a1D)
print(a1D_copy)