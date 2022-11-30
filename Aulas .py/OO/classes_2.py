class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def exibir_livros(self):
        for livro in self.__livros:
            print(livro)

    @property
    def livros(self):
        return self.__livros

    @property
    def nome(self):
        return self.__nome

    def __del__(self):
        print(f"A biblioteca - {self.nome} - foi desmantelada.")

    ###########################################################################
    def __len__(self):
        return len(self.__livros)

    def __bool__(self):
        return len(self.__livros) > 0

    def __add__(self, other):
        for livro in other.livros:
            self.__livros.append(livro)
            #Poderíamos criar e retornar uma bilioteca nova

    def __radd__(self, other):
        return other + len(self)