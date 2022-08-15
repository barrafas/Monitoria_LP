#Utilizando a cláusula Else em exceções
#O que acontece quando utilizamos raise sem especificar uma exceção?
'''
try:
    with open("emap.txt") as file:
        read_data = file.read()
except FileNotFoundError as fnfe:
    print(dir(fnfe))
    print("Arquivo não existe!", fnfe)
    #A exceção ativa será lançada
    #raise
else:
    print("Nenhum erro ocorreu, arquivo encontrado!")

print("Estamnos fora do bloco Try Except")
#E aqui?
#raise
'''

#Utilizando a cláusula Finally em exceções
#Usando "from" para cadeia de exceções
'''
def eu_adoro_a_emap(): #Amor incondicional, não preciso de argumentos!
    return 1/0

try:
    resultado = eu_adoro_a_emap()
except ZeroDivisionError as zde:
    print("Vida dura, amiguinho!", zde)
    #Exception chaining
    # raise RuntimeError from zde
else:
    print("Parabéns, amiguinho!")
finally:
    print("Aqui você deve executar suas rotinas de limpeza")
'''

#Agora um exemplo onde o except não funciona, apenas trocando o ZeroDivisionError por FileNotFoundError

'''
try:
    resultado = eu_adoro_a_emap()
except FileNotFoundError as fnfe:
    print("Vida dura, amiguinho!", zde)
    #Exception chaining
    #raise RuntimeError from zde
else:
    print("Parabéns, amiguinho!")
finally:
    print("Aqui você deve executar suas rotinas de limpeza")
# A exceção é re-lançada após o Finally
'''

#Existem muitas regras com return, break, continue, etc. Não queremos ver todas, mas temos que entender a complexidade
'''
def parece_facil():
    try:
        return True
    finally:
        return False

print(parece_facil())
'''

'''
numeros = [42]

assert numeros[0] != 42, "Esperamos um número diferente de 42"
assert 42 in numeros[0], "Esperamos o elemento 42 na lista"

assert isinstance(numeros[0], int), "Esperamos um número inteiro"
assert type(numeros[0]) == int, "Esperamos um número inteiro"
'''