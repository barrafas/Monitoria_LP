'''
#Syntax Error - Sem Execução!
if 1 > 2
    print("O que está errado não pode estar certo!")
'''

#Exception Errors - chamamos de levantar ou lançar uma exceção
'''
lista = [10, 20, 30, 40, 50]
print(lista[5])
'''
'''
lista = [10, 20, 30, 40, 50]
print(liste[5]) #Repare que apenas este erro é reportado
print(lista[5])
'''

#Q: O que está acontecendo?
#A: A execução é interrompida, pois o programa não sabe se recuperar.

'''
numero = int(input("Digite um número inteiro: "))
print(numero) #Utilizar 5, 5.0 e "Oi"
print(10/numero) #Utilizar 0
'''

#Mais um exemplo
'''
with open("minhas_ferias.txt") as file:
    read_data = file.read()
'''

#Também podemos fazer manualmente
'''
raise FileNotFoundError("Mensagem de Erro")
'''

#Vamos tratar a exceção
'''
def divisao_arriscada(a, b):
    return a/b

resultado = divisao_arriscada(3,3)
print(resultado)
'''

#Opção 1: Direto onde ocorre o problema
'''
def divisao_arriscada(a, b):
    try:
        return a/b
    except:
        print("Retornando para segurança do fluxo principal")
        return "Algo deu errado!"

resultado = divisao_arriscada(3,0)
print(resultado)
resultado = divisao_arriscada(3,3)
print(resultado)
'''

#Opção 2: Em torno de onde ocorre o problema
'''
def divisao_arriscada(a, b):
    return a/b

try:
    resultado = divisao_arriscada(3,0)
except:
    resultado = "Algo deu errado!"

print(resultado)

try:
    resultado = divisao_arriscada(3,3)
except:
    resultado = "Algo deu errado!"

print(resultado)
'''

#Sendo mais específico
'''
try:
    numero = int(input("Digite um número inteiro: "))
    print(10/numero) #Utilizar 5, 5.0 e "Oi"
except:
    print("Utilize os tipos corretos, amiguinho!")
    print("Divisão por zero não rola, amiguinho!")

try:
    numero = int(input("Digite um número inteiro: "))
    print(10/numero) #Utilizar 5, 5.0 e "Oi"
except ZeroDivisionError:
    print("Divisão por zero não rola, amiguinho!")
except ValueError:
    print("Utilize os tipos corretos, amiguinho!")
'''

#Exercício:
#Escrever uma função e proteger o programa da passagem de argumentos do tupo errado (int x list)