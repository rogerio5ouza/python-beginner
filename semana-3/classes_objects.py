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
