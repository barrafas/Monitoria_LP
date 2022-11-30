from classes_2 import Biblioteca

biblioteca1 = Biblioteca("Estante do Tio Rafa")
biblioteca1.adicionar_livro("Meditations")
biblioteca1.adicionar_livro("How to Grow Old")
biblioteca1.adicionar_livro("Enchiridion")

biblioteca1.exibir_livros()
print(biblioteca1.livros)

biblioteca2 = Biblioteca("Sala do Yuri")
biblioteca2.adicionar_livro("Álgebra Linear")
biblioteca2.adicionar_livro("Álgebra Linear e suas aplicações")
biblioteca2.adicionar_livro("Álgebra Linear com aplicações")

biblioteca2.exibir_livros()
print(biblioteca2.livros)

biblioteca3 = Biblioteca("Biblioteca do Museu Nacional")
biblioteca3.exibir_livros()
print(biblioteca3.livros)

# Operadores Python:    https://www.w3schools.com/python/python_operators.asp

print(len(biblioteca1))
print(len(biblioteca2))
print(len(biblioteca3))

if biblioteca1:
    print("Passei no print! - 1")
if biblioteca2:
    print("Passei no print! - 2")
if biblioteca3:
    print("Passei no print! - 3")

biblioteca1 + biblioteca2

biblioteca1.exibir_livros()
print(len(biblioteca1))
print(biblioteca1.livros)

print(3 + biblioteca1)