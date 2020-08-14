'''
Python Iterators

Um Iterator é um objeto que contém um número contável de valores.
Que pode ser iterado, o que significa que podemos percorrer todos os valores.
Tecnicamente, em Python, um Iterator é um objeto que implementa o protocolo do Iterator, que consiste nos métodos __iter__() e __next__().

Iterator vs Iterable

Lists, tuples, dictionaries e sets são todos objetos iteráveis. Eles são contêineres iteraveis dos quais podemos obter um Iterator.
Todos esses objetos possuem um método iter() que é usado para obter um Iterator.
'''
# Exemplo:
# Retorna um Iterator de uma tupla e, imprime cada um de seu valor:
minha_tuple_frutas = ('apple', 'banana', 'cherry', 'orange', 'melon')
meu_iterator = iter(minha_tuple_frutas)

print(next(meu_iterator))
print(next(meu_iterator))
print(next(meu_iterator))
print(next(meu_iterator))
print(next(meu_iterator))

# Até mesmo Strings são objetos iráveis e podem retornar um Iterator.
# Exemplo:

minha_string = 'banana'
meu_iterator_2 = iter(minha_string)

print(next(meu_iterator_2))
print(next(meu_iterator_2))
print(next(meu_iterator_2))
print(next(meu_iterator_2))
print(next(meu_iterator_2))
print(next(meu_iterator_2))

'''
Looping Through an Iterator

Podemos ainda, usar um loop FOR para iterar através de um objeto iterável.
'''
# Exemplo:
# Iterar os valores de uma Tuple:

minha_tuple_frutas_2 = ('maca', 'banana', 'cereja')

for frutas in minha_tuple_frutas_2:
    print(frutas)

# Iterar os caracteres de uma String:

minha_string_fruta = 'cereja'

for fruta in minha_string_fruta:
    print(fruta)

# O laço For cria um objeto Iterador e executa o método next() para cada laço.

'''
Create an Iterator

Para criar um objeto/classe como um Iterator, implementamos os métodos __iter__() e __next__() em seu objeto.

Como vimos em Classes/Objetos do Python, todas as classes têm uma função chamada __init__(), que permite que façamos algumas inicializações quando
o objeto está sendo criado.

O método __iter__() atua de forma semelhante, podemos fazer operações (inicializaçõe, etc.), mas devemos sempre retornar o próprio objeto Iterador.

O método __next__() também permite que façamos operações que deve retornar o próximo item na sequência.
'''
# Exemplo:
# Cria um Iterador que retorne números, começando com 1, e cada sequência aumentará em um (retornando 1,2,3,4,5 e etc.):


class meus_numeros:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


minha_classe = meus_numeros()
meu_iterator_3 = iter(minha_classe)

print(next(meu_iterator_3))
print(next(meu_iterator_3))
print(next(meu_iterator_3))
print(next(meu_iterator_3))
print(next(meu_iterator_3))


'''
StopIteration

O exemple acima continuaria para sempre se tivéssemos instruções next() suficientes ou se fosse usado em um loop For.

Para evitar que a iteração continue indefinidamente, podemos usar a instrução StopIteration.

No método __next__(), podemos adicionar uma  condição de término para gerar um erro se a iteração for feita um número específico de vezes.
'''
# Exemplo:
# Pare após 20 iterações:


class meus_numeros_2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


minha_classe_2 = meus_numeros_2()
meu_iterator_4 = iter(minha_classe_2)

for x in meu_iterator_4:
    print(x)
