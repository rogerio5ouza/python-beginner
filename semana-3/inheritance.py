'''
Pyhon Inheritance (Herança em Python)

A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.

Classe Pai é a classe que está sendo herdada, também chamada de classe Base.

Classe Filha é a classe que herda de outra classe, também chamada de classe Derivada.
'''
# Criando uma classe Pai


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def imprimeNome(self):
        print(self.nome, self.sobrenome)

# Usamos a classe Pessoa para criar um objeto e em seguida executamos o método imprimeNome:


p1 = Pessoa('Robert', 'Souza')
p1.imprimeNome()

'''
Child Clas (Classe Filha)

Para criarmos uma classe que herda a funcionalidade de outra classe, enviamos a classe Pai como parâmetro ao criar a classe Filha.
'''
# Exemlplo - Criação da classe Estudante que herdará as propriedades e os métodos da classe Pessoa:


class Pessoa2:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def imprimeNomeCompleto(self):
        print(self.nome, self.sobrenome)


class Estudante(Pessoa2):
    pass


e1 = Estudante('Eric', 'Matthes')
e1.imprimeNomeCompleto()

'''
Add the __init__() Function

Até o momento, criamos uma classe Filha que herda as propriedades e os métodos de sua classe Pai.

Vamos adicionar a função __init__() à classe Filha(em vez da palavra-chave pass).
'''
# OBS: A função __init__() é chamada automaticamente toda vez que a classe está sendo usada para criar um novo Objeto:


class Estudante2(Pessoa2):
    def __init__(self, nome, sobrenome):
        # add propriedades...

        # Quando Add a função __init__(), a classe Filha não herda mais a função __init__() da classe Pai:


class Pessoa3:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def imprimeNome(self):
        print(self.nome, self.sobrenome)


class Estudante3(Pessoa3):
    def __init__(self, nome, sobrenome):
        Pessoa3.__init__(self, nome, sobrenome)


p3 = Estudante3('Marijn', 'Haverbeke')
p3.imprimeNome()

'''
Uso da super() Function

Python também possui uma super() function que faz a classe Filha herdar todos os métodos e propriedades da classe Pai:
'''
# Exemplo:


class Pessoa4:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def imprimeNome(self):
        print(self.nome, self.sobrenome)


class Estudante4(Pessoa4):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)


p4 = Estudante4('Robert', 'C. Martin')
p4.imprimeNome()

# Obs: Ao usarmos a super() function, não precisamos usar o nome do elemento Pai, ele herdará automaticamente os métodos e propriedades da classe Pai.

'''
Add Properties
'''
# Add uma propriedade 'anoGraduacao' à classe Estudante5:


class Pessoa5:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def imprimeNome(self):
        print(self.nome, self.sobrenome)


class Estudante5(Pessoa5):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.anoGraduacao = 2020


p5 = Estudante5('Kent', 'Beck')
print(p5.anoGraduacao)
