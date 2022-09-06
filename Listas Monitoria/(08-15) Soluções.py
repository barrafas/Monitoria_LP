'''
===================================================================
1 - Crie uma função que receberá diversas alturas através de inputs 
(em algum loop) e retornará a média delas. Essa função deve ser pro-
tegida contra entrada de valores inválidos.
===================================================================
'''

def media_alturas():
    resultado = 0
    contador = 0
    while True:
        try:
            altura = input('Digite uma altura válida em centimetros, digite "fim" para sair e ver o resultado.\n')
            altura = altura.strip().lower()
            if altura == "fim" and contador != 0:
                return resultado/contador
            if altura == "fim":
                return 0
            altura = float(altura)
            if altura < 0:
                raise ValueError()
            else:
                resultado += altura
                contador += 1
        except ValueError:
            print('Valor inválido, por favor digite um número maior que 0. Se quiser usar decimais, escreva com ponto ao invés de vírgula.')

'''
===================================================================
2 - Crie uma função que receberá um path para um arquivo .txt, irá
abrí-o em modo read, e caso o arquivo não exista, irá criá-lo.
===================================================================
'''

def abre_arquivo(path: str):
    try:
        arquivo = open(path, 'r')
        print(arquivo.read())
        return arquivo
    except FileNotFoundError:
        arquivo = open(path, 'w')
        print('Arquivo não encontrado, mas foi criado com sucesso!')
        return arquivo

'''
===================================================================
3 - Crie uma função que receberá duas listas de números e retornará
uma nova lista que é uma soma das duas listas. 

Ela deve ser protegida contra entrada de valores inválidos e, caso
as listas sejam de tamanhos diferentes, deve ser retornado uma men-
sagem ao usuário.

Exemplo 1:
[1, 3, 4, 6]
[2, 8, 11, 1]

Output:
[3, 11, 15, 7]


Exemplo 2:
[1, 5]
[4, 2, 8]

Output:
"Tamanhos não compatíveis!"
===================================================================
'''

def soma_listas(lista_1: list, lista_2: list):
    try:
        if (type(lista_1) != list) or (type(lista_2) != list):
            raise TypeError("Um dos argumentos não é uma lista.")
        if len(lista_1) != len(lista_2):
            return "Tamanhos não compatíveis!"
        resultado = []
        for x in range(len(lista_1)):
            resultado.append(float(lista_1[x]) + float(lista_2[x]))
        return resultado
    except (TypeError, ValueError) as error:
        return error

'''
===================================================================
4 - Crie uma função que receberá uma lista de nomes e irá lançar
uma exceção caso algum nome seja inválido.

Um nome é inválido quando:
- Não for uma string
- Tiver números
- Tiver um dos seguintes caracteres: "!@#$%¨&*()_+=-{}[]|:;<>,.?/

O tipo de exceção lançada deve ser diferente para cada um dos três
tipos de nomes inválidos. (Use raise Exception())
===================================================================
'''

def valida_nomes(lista_nomes: list):
    invalidos = '"!@#$%¨&*()_+=-{}[]|:;<>,.?/'
    if type(lista_nomes) != list:
        raise TypeError('O parâmetro deve ser uma lista.')
    for nome in lista_nomes:
        if type(nome) != str:
            raise TypeError('Sua lista continha algum elemento não string.')
        for caracter in nome:
            if caracter in invalidos:
                raise ValueError(f"Há um carcterer inválido no nome: {caracter}")
            if caracter.isdigit():
                raise ValueError(f"Há um número no nome: {caracter}")
    return True

'''
===================================================================
5 - Crie uma função fatorial para os números inteiros não negativos
retorne o fatorial do número (exemplo 4!=24, 1!=1). Para criar essa 
função não é permitido utilizar bibliotecas, apenas o python 
padrão. Proteja a função para qualquer tipo de dados que seja
diferente dos números inteiros não negativos (-5! = exceção).
===================================================================

'''

def fatorial(numero: int):
    if type(numero) != int:
        raise TypeError("O parâmetro deve ser um número inteiro.")
    if numero < 0:
        raise ValueError("O parâmetro deve ser um número inteiro não negativo.")
    resultado = 1
    for x in range(1, numero+1):
        resultado *= x
    return resultado

