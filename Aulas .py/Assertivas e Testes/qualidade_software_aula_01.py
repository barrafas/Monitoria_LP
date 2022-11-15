import sys
 
sys.path.insert(0, "./src")
sys.path.insert(0, "./test")

import modulo_qualidade as mq
import test_modulo_qualidade as tmq

#O código abaixo ilustra como testávamos o código no período passado, invocando
#as funções testadas com diferentes combinações de parâmetros

print(mq.funcao_mais_simples_do_mundo(1, 1))
print(mq.funcao_mais_simples_do_mundo(-1, -1))
print(mq.funcao_mais_simples_do_mundo(1.0, 1.0))
print(mq.funcao_mais_simples_do_mundo(-1.0, -1.0))

try:
    print(mq.funcao_mais_simples_do_mundo(42, "Olá Amiguinhos"))
    #print(mq.funcao_mais_simples_do_mundo(42, True))
except AssertionError as error:
    print("Operandos Inválidos: ", error)

print(mq.soma("Olá Amiguinhos", 1))

#Demonstrando o comportamento de diferentes tipos de Docstring
#help(tmq)
#help(mq)
#help(mq.soma_correta)