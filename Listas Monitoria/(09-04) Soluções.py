import numpy as np
import numpy.random as npr

'''
===================================================================
1 - Usando apenas o conceito de "máscaras" (usar uma array de boo-
leanas para selecionar elementos de outra array), crie uma função
que receba um argumento m e n e retorne uma array mxn com valores
gerados aleatoriamente.
Você deve gerar uma array com uma distribuição normal de média 7
e desvio padrão 2, e após disso, você deve implementar um limite
de valores: os elementos da array devem ser, no máximo, 10, e no mí-
nimo, 0.
===================================================================
'''

def normalComLimite(m,n):
	array = npr.normal(7, 2, (m, n))
	array[array < 0] = 0
	array[array > 10] = 10
	return array

'''
===================================================================
2 - Novamente usando o conceito de máscaras, crie uma função que
irá receber uma array mxn que representa notas de alunos em uma
disciplina, onde cada linha representa um aluno e cada coluna a
nota de uma prova, que vale 10. A função deverá retornar uma array
mx1 de booleanas, cujo valor de cada linha deverá indicar True se o
aluno daquele índice tirou acima de 7 em ao menos metade das provas,
e False caso contrário.
===================================================================
'''

def alunosAprovados(notas):
    if notas.ndim == 1:  # Sem isso a função dá erro com arrays 1D
        notas = notas.reshape(1, -1)
    min_aprovacao = notas.shape[1] / 2
    trues = np.count_nonzero(notas>7, axis=1, keepdims=True)
    return (trues > min_aprovacao).flatten()

'''
===================================================================
3 - Usando apenas o conceito de broadcasting numpy (ou seja, sem
usar outras bibliotecas), crie uma função que receba uma array 1xn
e retorne uma array 1xn que é a "normalização Z-score" dela.
===================================================================
'''

def normalizarZScore(array):
	mean = array.mean()
	std = array.std()
	array = (array - mean)/std
	return array

'''
===================================================================
4 - Crie uma função que receberá uma array mxn que representa notas
de alunos da mesma forma que na questão 2, e retorne uma array mx1
de booleanas, cujo valor de cada linha deverá indicar True se o a-
luno daquele índice deverá ficar de recuperação, ou False caso não.
Um aluno deverá ficar de recuperação se a média das notas dele for
menor que 7 mas maior que 5.
===================================================================
'''

def recuperacao(array):
    mean = np.mean(array, axis=1)
    return (mean>5)&(mean<7)

'''
===================================================================
5 - Crie uma função que receberá uma array mxn de inteiros e que
retornará uma array mxn cujos elementos são o fatorial dos elemen-
tos da array de entrada.
Para aplicar o fatorial em cada elemento, não será permitido usar
loops. Tente pesquisar sobre a função "vectorize" do numpy.
===================================================================
'''

def fatorialArray(array):
    # "otypes=[object]" é para não dar erro de overflow com números grandes
    return np.vectorize(np.math.factorial, otypes=[object])(array)
