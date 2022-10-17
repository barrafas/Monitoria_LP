import numpy as np
import numpy.random as npr

"""
1 - (a) (1 ponto) Elabore uma funcão que recebe um inteiro n e retorna o n-ésimo número de
Fibonacci. Realize o tratamento de exceções, se necessário.
"""

def Questao1a(n):
    try:
        if n <= 0:
            raise ValueError("O índice precisa ser positivo!")
        if type(n) == float:
            raise TypeError("Não há índice decimal!")
        if n == 1:
            return 0
        if n == 2:
            return 1  
        return Questao1a(n-1) + Questao1a(n-2)
    except Exception as error:
        return error   

"""
(b) (1 ponto) Elabore uma função que recebe um inteiro n e retorna um NumPy Array com
todos os números de Fibonacci menores que n. Realize o tratamento de exceções, se
necessário.
"""

def Questao1b(n):
    try:
        if type(n) != int:
            raise TypeError
        fib_array = []
        k = 0
        while True:
            fib_k = Questao1a(k)
            if fib_k >= n:
                break
            fib_array.append(fib_k)
            k += 1        
        return np.array(fib_array)
    except TypeError:
        return "Entrada inválida: não é um inteiro"
    except Exception as ex:
        return ex

"""
(c) (1 ponto) Elabore uma função que recebe um inteiro n e retorna verdadeiro se n ́e número
de Fibonacci e falso caso contrário. Realize o tratamento de exceções, se necessário.
"""

def Questao1c(n):
    try:
        if n in Questao1b(n+1):
            return True
        return False
    except TypeError:
        return "Entrada inválida: não é um inteiro"
    except Exception as ex:
        return ex

"""
(d) (1 ponto) Elabore uma função que recebe um NumPy Array de inteiros entre 0 e 1.000
e retorna um NumPy Array de booleanos indicando se os elementos do NumPy Array
recebido são números de Fibonacci. P.ex. a função recebe [0 5 10] e retorna [True True
False].
"""

def Questao1d(arr: np.array):
    try:
        if np.any(arr < 0) or np.any(arr > 1000):
            raise ValueError("Não pode haver número menor que 0 ou maior que 1000")
        fibo = Questao1b(1001)
        return np.isin(arr, fibo)
    except Exception as error:
        return error

"""
2 - Elabore uma função que recebe os dados necessários para calcular uma série de pagamentos
baseado na Tabela Price (Valor da Parcela, Valor Presente, Taxa de Juros e Período).
A função deve retornar um NumPy Array 3 x n com o valor atual mês a mês da dívida, da
amortização e dos juros pagos
"""

def Questao2(par, valor, juros, periodo):
    try:
        if par < 0:
            raise ValueError("A parcela precisa ser positiva ou 0")
        if valor < 0:
            raise ValueError("O valor precisa ser positiva ou 0")
        if juros < 0:
            raise ValueError("O juros precisa ser positiva ou 0")
        if type(periodo) != int:
            raise TypeError("O valor do periodo deve ser inteiro!")    
        if periodo <= 0:
            raise ValueError("O periodo precisa ser positiva")
        valores = [valor]
        juros_pago = [0]
        amortizacao = [np.nan]

        for i in range(periodo):
            juros_atual = valores[-1] * juros / 100
            amortizacao_atual = par - juros_atual
            valore_atual = valores[-1] - amortizacao_atual
            
            if valore_atual < 0:
                amortizacao_atual += valore_atual
                valore_atual = 0
                
            juros_pago.append(juros_pago[-1] + juros_atual)
            amortizacao.append(amortizacao_atual)
            valores.append(valore_atual)
            
            if valore_atual <= 0:
                break
        return np.array([valores,juros_pago, amortizacao])
    except Exception as error:
        return error


"""
3 - (a) (1 ponto) Elabore uma função que recebe um inteiro n gera um NumPy Array de tamanho
n com números de ponto flutuante entre 1 e 5. Estes números simulam notas dadas a
um restaurante. Realize o tratamento de exceções, se necessário.
"""

def Questao3a(n):
    try:
        if n < 0:
            raise ValueError("Entrada inválida: inteiro negativo")
        if type(n) != int:
            raise TypeError("Entrada inválida: não é um inteiro")
        return npr.uniform(1,5,n)
    except Exception as error:
        return error

"""
(b) (1 ponto) Elabore uma função que recebe dois NumPy Arrays (um, simulando notas de
críticos e outro simulando notas de clientes regulares) de tamanho n e retorna um NumPy
Array 2 x n através do empilhamento dos arrays recebidos. As notas dos críticos possuem
peso triplo, ent ao você deve utilizar a propriedade de Broadcast para multiplicar as notas
antes de retornar o NumPy Array 2 x n.
"""

def Questao3b(ntCriticos, ntClientes):
    try:
        if ntCriticos.shape != ntClientes.shape:
            raise ValueError("Os arrays precisam ter o mesmo tamanho")
        empilhadas = np.vstack((ntCriticos, ntClientes))
        empilhadas[0,:] = empilhadas[0,:] * 3
        return empilhadas
    except Exception as error:
        return error


"""
(c) (1 ponto) Elabore uma função que recebe um NumPy Array 2 x n e exibe ao menos 3
metadados do Array e 3 informações estatísticas.
"""

def Questao3c(array):
    try:
        if array.ndim != 2:
            raise ValueError("O array precisa ter somente 2 linhas")
        print("Dimensão:", array.ndim)
        print("Forma:", array.shape)
        print("Tamanho:", array.size)
        print("Média:", np.mean(array))
        print("Desvio Padrão:", np.std(array))
        print("Mínimo:", np.min(array))
    except Exception as error:
        print(error)
        return error

