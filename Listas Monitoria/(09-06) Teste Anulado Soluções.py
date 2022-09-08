import numpy as np

# OBS: Exemplos importantes de saber de numpy:

"""
OBS: Para usar lógica booleana em máscaras:
& é o "and"
~ é o "not"
| é o "or"
Exemplo: arr[(arr>5)|(arr<3)]
"""

arr = np.array([1, 7, 5, 3, 9])  # Array de elementos a serem avaliados
mascara = (arr>4) & (arr<8)  # A condição que será a máscara
print("Mascara: ", mascara)  # Mostrando as booleanas da máscara
print("Array filtrada: ", arr[mascara])  # Mostrando os elementos da array que cumprem a condição
arr[mascara] = 5  # Definindo que todos os elementos que cumprem a condição são iguais a 5
print("Array modificada: ", arr)  # Mostrando array final


print("Bool arr > 2:", arr > 2)
print("Any:", np.any(arr > 2))  # Retorna True se qualquer valor da array for True
print("All:", np.all(arr > 2))  # Retorna True se apenas todos os valores forem True

"""
============================================================================
1 a- Elabore uma função que recebe um inteiro n e retorna o n-ésimo número 
de Fibonacci. Realize o tratamento de exceções, se necessário.
============================================================================
"""

def Fibonacci(n: int):
    try:
        if n < 0:
            raise ValueError("O índice precisa ser positivo!")
        if type(n) == float:
            raise TypeError("Não há índice decimal!")
        ind0 = 0
        ind1 = 1
        for num in range(0, n-1):
            ind0, ind1 = ind1, ind0+ind1
        return ind0
    except Exception as error:
        return error

#print(Fibonacci(1))


"""
============================================================================
1 b- Elabore uma função que recebe um inteiro n e retorna uma array com todos 
os números de Fibonacci menores que n.
============================================================================
"""
    
def FibonacciArray(n: int):
    try:
        if type(n) == float:
            raise TypeError("Não há índice decimal!")
        lista = []
        ind0 = 0
        ind1 = 1
        while ind0 < n:
            lista.append(ind0)
            ind0, ind1 = ind1, ind0+ind1
        return np.array(lista)
    except Exception as error:
        return error

#print(FibonacciArray(10000))
    
"""
============================================================================
1 c- Elabore uma função que recebe um array de inteiros e retorna um array 
de booleanos indicando se os elementos do recebido são números de Fibonacci.
============================================================================
"""

def FibonacciBool(arr: np.array):
    try:
        if np.any(arr < 0) or np.any(arr > 1000):
            raise ValueError("Não pode haver número menor que 0.")
        fibo = FibonacciArray(1001)
        return np.isin(arr, fibo)
    except Exception as error:
        return error



"""
============================================================================
2 a- Elabore uma função que recebe um inteiro n e retorna uma array de tama-
nho n com valores entre 1 e 5.
============================================================================
"""

def UniformeGen(n: int):
    try:
        if n < 0:
            raise ValueError("O índice precisa ser positivo!")
        if type(n) == float:
            raise TypeError("Não há índice decimal!")
        arr = np.random.uniform(1, 5, n)
        return arr
    except Exception as error:
        return error

# print(UniformeGen(15))

"""
============================================================================
2 b- Elabore uma função que recebe dois NumPy Arrays (um, simulando notas de 
críticos e outro simulando notas de clientes regulares) de tamanho n e re-
torna uma array 2xn através de empilhamento dos arrays recebidos. As notas
dos críticos possuem peso triplo. 
OBS: Para realizar a multiplicação você deve selecionar os elementos através
de slicing após construir o array 2xn e utilizar uma UFunc.
============================================================================
"""

def Notas(arrCrit: np.array, arrReg: np.array):
    try:
        if arrCrit.size != arrReg.size:
            raise ValueError("Os arrays precisam ter o mesmo tamanho!")
        arr = np.vstack((arrCrit, arrReg))
        arr[0] = np.multiply(arr[0], 3)
        return arr
    except Exception as error:
        return error

result = Notas(UniformeGen(5), UniformeGen(5))
# print(result)

"""
============================================================================
2 c- Elabora uma função que recebe um NumPy Array 2xn e exibe ao menos 3 me-
tadados do Array e 3 informações estatísticas.
============================================================================
"""

def Info(arr: np.array):
    try:
        if arr.ndim != 2:
            raise ValueError("O array precisa ser 2xn!")
        print("DType:", arr.dtype)
        print("Tamanho:", arr.size)
        print("Forma:", arr.shape)
        print("Média:", np.mean(arr))
        print("Desvio Padrão:", np.std(arr))
        print("Máximo:", np.max(arr))
    except Exception as error:
        return error

# Info(result)