'''
===================================================================
1 - Usando apenas o conceito de "máscaras" (usar uma array de boo-
leanas para selecionar elementos de outra array), crie uma função
que receba um argumento n e retorne uma array mxn com uma distribu-
ição normal de média 7 e desvio padrão 2, com uma característica
especial: os elementos da array devem ser, no máximo, 10, e no mí-
nimo, 0.
===================================================================
''' 

def normalComLimite(m,n):
	return

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
	return


'''
===================================================================
3 - Usando apenas o conceito de broadcasting numpy (ou seja, sem 
usar outras bibliotecas), crie uma função que receba uma array 1xn 
e retorne uma array 1xn que é a "normalização Z-score" dela.  
===================================================================
'''

def normalizarZScore(array):
	return

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
	return 

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
	return