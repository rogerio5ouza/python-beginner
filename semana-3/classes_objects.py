'''
Classes and Objects (Classes e Objetos)

Quase tudo no Python é um objeto, com suas propriedades e métodos.
Uma classe é como um construtor de objetos ou um modelo para criar objetos.
'''
# Exemplo:


class MinhaClasseNome:
    nome = 'roger'


print(MinhaClasseNome)

# Criação do objeto nome1 e impressão do valor nome:

nome1 = MinhaClasseNome()
print(nome1.nome)

'''
The __init__() Function 

Para entender o significado das classes, precisamos entender a função interna __init__().

Todas as classes têm uma função chamada __init__(), que é sempre executada quando a classe está sendo iniciada.

Usamos a função __init__() para atribuir valores às propriedades do objeto ou outras operações necessárias quando o objeto estiver sendo criado.
'''
# Exemplo:


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Robert', 32)

print(p1.nome)
print(p1.idade)

'''
Object Methods (Métodos de objeto)

Objetos também podem conter métodos. Métodos em objetos são funções que pertencem ao objeto.

'''
# Exemplo:


class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def minhaFunc(self):
        print('Olá, meu nome é: ' + self.nome)


p1 = Pessoa2('Roger', 32)
p1.minhaFunc()

'''
The self Parameter (O Parâmetro self)

O parâmetro self é uma referencia a instância atual da classe e é usado para acessar variáveis que pertencem à classe.

Ele não precisa ser nomeado como self, podemos chamá-lo como quisermos, mas dever ser o primeiro parâmetro de qualquer função da classe.
'''
# Exemplo:


class Pessoa3:
    def __init__(meuparametro, nome, idade):
        meuparametro.nome = nome
        meuparametro.idade = idade

    def minhaFunc(abc):
        print('Olá, meu nome é: ' + abc.nome)


p1 = Pessoa3('Roger', 32)
p1.minhaFunc()
