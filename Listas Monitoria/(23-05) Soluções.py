# 1- Faça um código que irá receber uma lista de dicionários e irá
# concatená-los em um único novo dicionário. Caso uma mesma chave esteja
# presente em mais de um dicionário, some seus valores.

dics = [{"final fantasy":14, "persona":4},
       {"persona":3, "elden ring":1},
       {"hollow knight":11, "celeste":40}]

output1 = {}

for dic in dics:
    for item in dic.items():
        if item[0] in output1.keys():
            output1[item[0]] += item[1]
        else:
            output1[item[0]] = item[1]

print("===================================================================")
print("Output 1: ", output1)
print("===================================================================\n")



# 2- Faça um código que irá converter uma string para um dicionário.

string = "batata frita"

output2 = {}

for letter in string:
    if letter in output2.keys():
        output2[letter] += 1
    elif letter != " ":
        output2[letter] = 1

print("===================================================================")
print("Output 2: ", output2)
print("===================================================================\n")



# 3- Defina uma função que irá receber um dicionário de nomes,
# peso e altura, e também irá receber um peso e uma altura.
# Essa função deverá retornar um novo dicionário, contendo apenas os
# nomes cujo peso e altura sejam acimas dos recebidos pela função.

dicionario = {"Tiago": (166.5, 60),
 			  "Batata": (172, 71),
 			  "Teclado": (156, 48)}

def checaPesoAltura(dicionario, peso, altura):
    output3 = {}
    for item in dicionario.items():
        if item[1][0] > peso and item[1][1] > altura:
            output3[item[0]] = item[1]
    return output3

output3 = checaPesoAltura(dicionario, 160, 62)

print("===================================================================")
print("Output 3: ", output3)
print("===================================================================\n")



# 4- Crie uma função que implementará uma forma de "Binary Search".
# Dado uma lista ordenada de forma crescente e um valor, essa função
# irá retornar verdadeiro caso o item esteja na lista, e falso caso
# não esteja.

# OBS: Não use "is in", pesquise um pouco sobre o conceito
# de binary search e tente implementá-lo manualmente.
# (basicamente, ele checa o meio da lista e vê se o item
# está antes ou depois do meio, sempre cortando a lista pela metade
# até encontrar ou não o item desejado)

lista = [1,2,3,5,7,11,13,17,23,29]

def isIn(lista, item):
    start = 0
    mid = len(lista) // 2
    end = len(lista) - 1
    while start <= end:
        if lista[mid] == item:
            return True
        elif lista[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
    return False


output4 = isIn(lista, 4)

print("===================================================================")
print("Output 4: ", output4)
print("===================================================================\n")



# 5- Dado uma lista de tamanho n de tuplas de 2 elementos, 
# retorne uma outra lista contendo duas tuplas de tamanho n.

# OBS: Esse tipo de operação é comumente chamada de "zip"

lista = [(2, 7), (5, 14), (11, 15)]

output5 = []
i = 0

while i < len(lista[0]):
    listatemp = []
    for tupla in lista:
        listatemp.append(tupla[i])
    output5.append(tuple(listatemp))
    i+=1

print("===================================================================")
print("Output 5: ", output5)
print("===================================================================\n")
    


# 6- Dado uma lista de tuplas de valores numéricos, 
# retorne uma tupla que contém a soma de cada indice de elementos

lista = [(1, 3, 5, 7),
         (-2, 4, 1, -5),
         (4, 8, 11, 1)]

output6 = []
i = 0

while i < len(lista[0]):
    soma = 0
    for tupla in lista:
        soma += tupla[i]
    output6.append(soma)
    i+=1

output6 = tuple(output6)

print("===================================================================")
print("Output 6: ", output6)
print("===================================================================\n")



# EXTRA - Crie uma função que receberá um dicionário e retornará
# esse mesmo dicionário, reordenado pelos valores.

# Dica: pesquise pela função sorted e o conceito de "funções lambda"

def ordenarDict(dicionario, ordem):
    if ordem == "crescente":
        return sorted(dicionario.items(), key=lambda x: x[1])
    elif ordem == "decrescente":
        return sorted(dicionario.items(), key=lambda x: x[1], reverse=True)
    else:
        print("Opção inválida")
        return dicionario

dicionario = {"vermelho": 90, "azul": 60, "verde": 120}
outputExtra = ordenarDict(dicionario, "crescente")

print("===================================================================")
print("Output EXTRA: ", outputExtra)
print("===================================================================\n")