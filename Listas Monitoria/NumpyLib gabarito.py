import numpy as np
import numpy.random as npr
import numpy.linalg as LA
from functools import reduce

'''
===================================================================
1 - Crie uma função usando numpy que caso receba uma matriz 
bidimensional numpy retorna um vetor unidimensional. Se a entrada é
um vetor unidimensional retorne uma matriz diagonal com os 
elementos do vetor. Caso contrário levante uma exceção ValueError.
===================================================================
''' 

def diagonalEspecial(D):
	try:
		if D.ndim == 2: # Caso o vetor seja bidimensional transforma-o em um unidimensional
			return D.flatten()
		elif D.ndim == 1: # Se o vetor for unidimensional, cria uma matriz diagonal com esse vetor
			return np.diagflat(D)
		else: # "Levanta" um ValueError se o vetor não for nem unidimensional nem bidimensional
			raise ValueError

	# Reporta ao usuário caso ocorra um ValueError decorrente de uma entrada de uma matriz inválida
	except ValueError:
		return "A entrada da função deve ser uma matriz bidimensional ou um vetor unidimensional!"

	# Caso a entrada seja inválida, retorna uma mensagem para o usuário
	except AttributeError:
		return "A entrada da função deve ser do tipo nparray!"

'''
===================================================================
2 - Crie uma função para simular o jogo pedra papel tesoura usando 
números aleatórios do numpy.
- Suponha que tirar pedra, papel ou tesoura possui a mesma 
probabilidade de acontecer.
- A entrada corresponde ao número de vezes que o experimento deve
acontecer.
- A função deve retornar um dicionário com a quantidade de vezes
que cada evento aconteceu (ex: {'papel':1,'pedra':3,'tesoura':2})
===================================================================
'''

# Função que cria a contagem de n jogadas
def criar_contagem(n):
	jogadas = npr.randint(0, 3, n) # Cria um vetor com n valores entre 0 e 2
	index, contagem = np.unique(jogadas, return_counts = True) # Faz a contagem dos valores únicos no vetor
	return dict(zip(index, contagem)) # Retorna o dicionário que possui a contagem dos seus respecivos indíces

# Função que altera as chaves de um dicionário
def alterar_chave(dict_antigo, chaves_novas):
	dict_novo = {} # Cria um dicionário vazio
	for chave in dict_antigo: 
		dict_novo[chaves_novas[chave]] = dict_antigo[chave] # Obtém os valores do dicionário antido, mas altera as chaves
	return dict_novo

def jokenpo(n):
	try:
		if type(n) != int: # Caso o tipo da entrada não seja um inteiro "levanta" uma exceção
			raise TypeError
		contagem = criar_contagem(n) # Cria a contagem de n jogadas
		resultado = alterar_chave(contagem, ["papel", "pedra", "tesoura"]) # Altera os índices de contagem para as possivilidades do jogo
	
	# Retorna uma mensagem para um erro de valor na entrada
	except ValueError: 
		return "O número de jogadas deve ser um inteiro positivo!" 
	
	# Retorna uma mensagem para um erro de tipo na entrada
	except TypeError: 
		return "A função não aceita valores que não sejam inteiros!"

	else:
		return resultado # Retorna o dicionário final

'''
===================================================================
4 - Crie uma função numpy que dada uma matriz A de dimensão mxn. 
Retorne um vetor um vetor coluna mx1 onde cada entrada i 
corresponde ao menor valor da linha i.
===================================================================
'''

def minimos(A):
    # Obtém os mínimos de cada linha e transforma o resultado em vetor coluna
	return A.min(1).reshape(A.shape[0], 1)

'''
===================================================================
5 - Sabemos que uma multiplicação de matrizes não é comutativa. 
Mas, em alguns casos é possível verificar que A*B = B*A. Crie uma 
função que dada duas matrizes ela retorna verdadeiro se A*B=B*A e
retorna falso caso contrário. Observe que quando A e B não são 
matrizes quadradas a função deve retornar falso, independente do 
tamanho de A e B.
===================================================================
'''

def AB_igual_BA(A, B):
	try:
		print(A, B)
		if A.ndim == 1: # Caso a matriz A tenha apenas 1 dimensão, força a criação de outra
			A = np.array([A])
		if B.ndim == 1: # Caso a matriz B tenha apenas 1 dimensão, força a criação de outra
			B = np.array([B])
		
		if A.shape[0] != A.shape[1] or B.shape[0] != B.shape[1] or A.shape != B.shape:
			return False

	# Caso a entrada seja inválida, retorna uma mensagem para o usuário
	except (TypeError, AttributeError):
		return "A entrada da função deve ser do tipo nparray!"

	else:
		AvezesB = np.matmul(A, B) # Calcula A*B
		BvezesA = np.matmul(B, A) # Calcula B*A
		return np.array_equal(AvezesB, BvezesA) # Retorna se as duas multiplicações são iguais

'''
===================================================================
6 - Crie uma função que recebe uma lista de vetores numpy, retorne 
o vetor que possuiu a menor norma vetorial. 

Desafio opcional: tente resolver essa questão com uma só linha de 
código, recomendo utilizar map e função lambda. Confira a seguir:

https://medium.com/horadecodar/express%C3%B5es-lambda-em-python-com-map-reduce-e-filter-a391368ae886
https://cs.stanford.edu/people/nick/py/python-map-lambda.html
===================================================================
'''

def menorNorma(l):
    # reduzimos a lista guardando sempre o vetor que tiver a menor norma
    vetor_menor_norma = reduce((lambda x,y: x if LA.norm(x) < LA.norm(y) else y), l)
    return vetor_menor_norma

'''
===================================================================
7 - Desafio, vamos estimar o valor de pi por meio do Método de 
Monte Carlo. Considere um círculo de raio r=1 centrado na origem 
que está inscrito num quadrado de lado l=2 (veja a figura pi.png).
Vamos estimar o valor de pi comparando a razão da quantidade de 
pontos P_c que "caíram" dentro do círculo (matematicamente P_c
representa o número de pontos em que a distância euclidiana deles
a origem é menor do que r) em relação ao total de pontos P com a
razão da área do círculo em relação ao quadrado, observe:
pi*r^2/l^2 ~= P_c/P
Isto é, utilizando os valores de r^2=1 e l^2=4 estime o valor de pi:
pi/4 ~= P_c/P 
A função que vocês devem implementar deve:
- Receber n como o número de pontos que serão gerados.
- Gerar com numpy n coordenadas x aleatórias.
- Gerar com numpy n coordenas y aleatórias.
- Calcular a quantidade P_c de pontos que caíram dentro do círculo, 
isto é, calcular a distância do ponto I=(x_i,y_i) à origem (0,0) e
contar quantos estão mais próximos da origem do que o raio do círculo
(r=1).
- Retornar o valor de Pi de acordo com a expressão pi = (4*P_c)/P.
Obs: para saber mais sobre o Método de Monte Carlo acesse:
https://pt.wikipedia.org/wiki/M%C3%A9todo_de_Monte_Carlo
===================================================================
'''

def piMonteCarlo(n):
	try:
		x_coord = npr.random(n) * 2 - 1 # Gera n coordenadas entre -1 e 1 para x
		y_coord = npr.random(n) * 2 - 1 # Gera n coordenadas entre -1 e 1 para y

	# Retorna uma mensagem para um erro de valor na entrada
	except ValueError: 
		return "A entrada da função deve ser um inteiro positivo!" 
	
	# Retorna uma mensagem para um erro de tipo na entrada
	except TypeError: 
		return "A função não aceita valores que não sejam inteiros!"

	else:
		distancias = np.emath.sqrt(x_coord**2 + y_coord**2) # Cria um array com a distância entre cada ponto e a origem
		p_c = (distancias < 1).sum() # Conta quantas distâncias são menores do que 1
		pi = (4*p_c)/n # Calcula o valor de pi
		return pi # Retorna o valor de pi econtrado

