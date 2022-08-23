import numpy as np

#Criação de ndarrays apenas com base em estruturas tradicionais
a1Da = np.array([1, 2, 3, 4])
a1Db = np.array([5, 6, 7, 8])
a1D = np.concatenate((a1Da, a1Db))
print("Elemento 1: ", a1D[0])
print("Slicing: ", a1D[2:6:2])
print(type(a1D), "\n", a1D, "\n")
print(f"Dados sobre a1D:\nDimensão: {a1D.ndim}\nForma: {a1D.shape}\nTamanho: {a1D.size}\nTipo: {a1D.dtype}")
print("===============================================================")
# Exemplo de propriedade. Buscar "NumPy itemsize"... print(f"Tamanho do elemento: {a1D.itemsize}")

#Estamos em C!
a2D = np.array([[1.0, 2.0], [3.0, 4.0]])
print("Elemento 1,1: ", a2D[0,0]) #Alguma diferença aqui ao comparar com um array tradicional?
print("Slicing: ", a2D[::-1,::-1]) #Alguma diferença aqui ao comparar com um array tradicional?
print(type(a2D), "\n", a2D, "\n")
print(f"Dados sobre a2D:\nDimensão: {a2D.ndim}\nForma: {a2D.shape}\nTamanho: {a2D.size}\nTipo: {a2D.dtype}")
print("===============================================================")

a3D = np.array([[[1, 2], [3, 4]],[[1, 2], [3, 4]]], dtype=np.float64)
print("Elemento 1,1,1: ", a3D[0,0,0]) #Alguma diferença aqui ao comparar com um array tradicional?
print(type(a3D), "\n", a3D, "\n")
print(f"Dados sobre a3D:\nDimensão: {a3D.ndim}\nForma: {a3D.shape}\nTamanho: {a3D.size}\nTipo: {a3D.dtype}")
print("===============================================================")