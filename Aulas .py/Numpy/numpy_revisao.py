import numpy as np

#Criação de ndarrays apenas com base em estruturas tradicionais
a1Da = np.array([1, 2, 3, 4])
a1Db = np.array([5, 6, 7, 8])
print("Elemento 1: ", a1Da[0])
print("Slicing: ", a1Da[2:6:2])
print(f"Dados sobre a1Da:\nDimensão: {a1Da.ndim}\nForma: {a1Da.shape}\nTamanho: {a1Da.size}\nTipo: {a1Da.dtype}\nTamanho do elemento: {a1Da.itemsize}")
print("=" * 40)

###############################################################################

#DICA 1: Reparar se o tipo e a quantidade de parâmetros está correta em métodos e funções NumPy
a1D = np.concatenate((a1Da, a1Db)) #Tupla
print("\n\nArray Concatenado: \n", a1D)
print(f"Dados sobre a1D:\nDimensão: {a1D.ndim}\nForma: {a1D.shape}\nTamanho: {a1D.size}\nTipo: {a1D.dtype}\nTamanho do elemento: {a1D.itemsize}")
a1D = np.vstack((a1Da, a1Db)) #Tupla!!!
print("\n\nArray Empilhado: \n", a1D)
print(f"Dados sobre a1D:\nDimensão: {a1D.ndim}\nForma: {a1D.shape}\nTamanho: {a1D.size}\nTipo: {a1D.dtype}\nTamanho do elemento: {a1D.itemsize}")
print("=" * 40)

#ERRO !!!
#a1D = a1D.reshape(5,2)

try:
    a1D = a1D.reshape(4,2)
except ValueError as error:
    print("Erro de conversão de forma.", error)
else:
    print("\n\nArray após Reshape: \n", a1D)
    print("\nElemento 1: ", a1D[0, 0])
    print("\nSlicing: ", a1D[1:4,:1])
finally:
    print("=" * 40)

###############################################################################
# Broadcast

print("\nSoma: ", a1D+42)
print("\nSubtração: ", a1D-42)
print("\nMultiplicação: ", a1D*42)
print("\nDivisão: ", a1D/42)
print("=" * 40)

###############################################################################
# Cópias Superficiais e Profundas

a1D = np.linspace(0, 100, 10)
print("\n\n", a1D)
a1D_copy = a1D
print("\n\n", a1D_copy)

#Eles são o mesmo objeto?
print(id(a1D))
print(id(a1D_copy))

a1D_copy[0] = 42
print("\n\n", a1D)
print("\n\n", a1D_copy)

#DICA 2: Funções normalmente retornam cópias dos NDArrays originais
outro_vetor = a1D.reshape(5,2)
outro_vetor[0,0] = 1000
print("\n\n", outro_vetor)
print("\n\n", a1D)

#O que está acontecendo? Estas cópias são superficiais 

a1D = np.arange(10)
a1D_copy = a1D.copy() #Deep Copy
print(id(a1D))
print(id(a1D_copy))

print("\n\n", a1D)
print("\n\n", a1D_copy)

a1D_copy[0] = 42
print("\n\n", a1D)
print("\n\n", a1D_copy)
print("=" * 40)