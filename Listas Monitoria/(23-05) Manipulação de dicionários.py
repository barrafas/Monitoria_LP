'''
===================================================================
1- Faça um código que irá receber uma lista de dicionários e irá
concatená-los em um único novo dicionário. Caso uma mesma chave esteja
presente em mais de um dicionário, some seus valores.

Exemplo: 
[{"final fantasy":14, "persona":4},
 {"persona":3, "elden ring":1},
 {"hollow knight":11, "celeste":40}]

Output:
{"final fantasy":14, "persona":7, "elden ring":1,
 "hollow knight":11, "celeste":40}
===================================================================
'''

'''
===================================================================
2- Faça um código que irá converter uma string para um dicionário.

Exemplo:
"batata frita"

Output:
{"b":1, "a":4, "t":3, "f":1, "r":1, "i":1}
===================================================================
'''

'''
===================================================================
3 - Defina uma função que irá receber um dicionário de nomes,
peso e altura, e também irá receber como argumento um peso e uma altura.
Essa função deverá retornar um novo dicionário, contendo apenas os
nomes cujo peso e altura sejam acimas dos recebidos pela função.

Exemplo:
dicionario = {"Tiago": (166.5, 60),
 				"Batata": (172, 71),
 				"Teclado": (156, 48)}
resultado = checaPesoAltura(dicionario, 160, 62)

Output:
{"Batata": (172, 71)}
===================================================================
'''

'''
===================================================================
4- Crie uma função que implementará uma forma de "Binary Search".
Dado uma lista ordenada de forma crescente e um valor, essa função
irá retornar verdadeiro caso o item esteja na lista, e falso caso
não esteja.

OBS: Não use "is in", pesquise um pouco sobre o conceito
de binary search e tente implementá-lo manualmente.
(basicamente, ele checa o meio da lista e vê se o item
está antes ou depois do meio, sempre cortando a lista pela metade
até encontrar ou não o item desejado)

Exemplo:
lista = [1,2,3,5,7,11,13,17,23,29]
booleana = isIn(lista, 4)

Output:
False
===================================================================
'''

'''
===================================================================
5- Dado uma lista de tamanho n de tuplas de 2 elementos, 
retorne uma outra lista contendo duas tuplas de tamanho n.

OBS: Esse tipo de operação é comumente chamada de "zip"

Exemplo:
[(2, 7), (5, 14), (11, 15)]

Output:
[(2, 5, 11), (7, 14, 15)]
===================================================================
'''

'''
===================================================================
6- Dado uma lista de tuplas de valores numéricos, 
retorne uma tupla que contém a soma de cada indice de elementos

Exemplo:
[(1, 3, 5, 7),
 (-2, 4, 1, -5),
 (4, 8, 11, 1)]

Output:
(3, 15, 17, 3)
===================================================================
'''

'''
===================================================================
EXTRA - Crie uma função que receberá um dicionário e retornará
esse mesmo dicionário, reordenado pelos valores.

Dica: pesquise pela função sorted e o conceito de "funções lambda"

Exemplo:
dicionario = {"vermelho": 90, "azul": 60, "verde": 120}
ordenado = ordenarDict(dicionario, "crescente")

Output:
{"azul": 60, "vermelho": 90, "verde": 120}
===================================================================
'''