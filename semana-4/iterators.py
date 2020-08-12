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
