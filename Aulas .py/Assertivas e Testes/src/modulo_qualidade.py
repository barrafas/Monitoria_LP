"""Título: Documentação de linhas múltiplas do módulo

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin malesuada est dignissim rhoncus posuere. Ut convallis orci sit amet commodo rhoncus. Aenean pharetra id orci ut mattis. Aliquam mi elit, ornare volutpat magna sit amet, pharetra dictum nisl. Donec faucibus luctus ligula nec feugiat.
Sed lobortis sem non ante dignissim accumsan vitae at tortor. Maecenas ultrices molestie lacus, quis ullamcorper diam aliquam vel. Proin egestas, augue ut pellentesque semper, tellus dui blandit est, a faucibus neque lorem non enim.
Suspendisse eu pharetra dui. Integer hendrerit tempus ex, ac vehicula orci sollicitudin in. Donec dolor ligula, euismod non purus in, ultricies ultrices odio. Morbi vulputate, risus non cursus euismod, justo eros egestas mauris, ultrices mollis sapien elit vitae neque. 

"""

# Vale a pena acrescentar tratamento de erro em uma função de soma DE INTEIROS para tratar os parâmetros não inteiros?
# Ver código comentado abaixo
def soma(a, b):
    """Uma linha simples explicando a funcao"""
    # Não podemos alterar os parâmetros imutáveis
    resultado = 0
    novo_a = ""

    if (not isinstance (a, int)):
        while (not isinstance (novo_a, int)):
            try:
                novo_a = int(input("Por favor digite um número inteiro para A: "))
            except ValueError as error:
                print("Valor inválido")
        resultado+=novo_a
    
    else:
        resultado+=a

    # Fazer o mesmo para B
    resultado+=b

    return resultado
    # E se a função trabalha com Inteiros ***E*** Decimais? Vamos perguntar ao usuário o que ele deseja...
    # e conferir se a resposta digitada é a correta

# O que estamos tentando fazer? Por que aumentar a complexidade da função?
# Uma função deve possuir quantas responsabilidades?
# O que acontece com a documentação e os testes quando uma função possui muitas responsabilidades?


# Uma assertiva é uma marcação utilizada para a comunicação em ambiente de desenvolvimento
# Se você dispara uma assertiva, percebe que o código foi utilizado de forma errada
# Ao utilizar a flag "-O" você solicita ao interpretador que ignore as assertivas

# Assertivas NÃO SÃO testes
def funcao_mais_simples_do_mundo(a, b):
    """Documentacao da funcao

    Explicacao detalhada da funcao
    Explicacao detalhada da funcao
    Explicacao detalhada da funcao

    >>> funcao_mais_simples_do_mundo(42, 42)
    84
    >>> funcao_mais_simples_do_mundo("Olá Amiguinhos", 42)
    Traceback (most recent call last):
    ...
    AssertionError: Primeiro operando não é int ou float
    """
    assert isinstance(a, (int, float)), "Primeiro operando não é int ou float"
    assert isinstance(b, (int, float)), "Segundo operando não é int ou float"
    return a + b

def soma_correta(numero_1, numero_2):
    """Soma dois números recebidos por parâmetro

    :param numero_1: Primeiro Número
    :type numero_1: int
    :param numero_2: Segundo Número
    :type numero_2: int
    :return: Soma de número 1 e número 2
    :rtype: int

    """
    return numero_1 + numero_2

def ler_temperatura():
    print("Código super difícil que lê um sensor IoT")
    return 0

def alerta_ponto_fulgor():
    temperatura = ler_temperatura()
    if temperatura > 16.6:
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)