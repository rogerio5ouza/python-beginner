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
