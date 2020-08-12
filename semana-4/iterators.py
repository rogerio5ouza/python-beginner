'''
Python Iterators

Um Iterathor é um objeto que contém um número contável de valores.
Que pode ser iterado, o que significa que podemos percorrer todos os valores.
Tecnicamente, em Python, um Iterathor é um objeto que implementa o protocolo do Iterathor, que consiste nos métodos __iter__() e __next__().

Iterathor vs Iterable

Lists, tuples, dictionaries e sets são todos objetos iteráveis. Eles são contêineres iteraveis dos quais podemos obter um Iterathor.
Todos esses objetos possuem um método iter() que é usado para obter um Iterathor.
'''
# Exemplo:
# Retorna um Iterathor de uma tupla e, imprime cada um de seu valor:
minha_tuple_frutas = ('apple', 'banana', 'cherry', 'orange', 'melon')
meu_iterathor = iter(minha_tuple_frutas)

print(next(meu_iterathor))
print(next(meu_iterathor))
print(next(meu_iterathor))
print(next(meu_iterathor))
print(next(meu_iterathor))

# Até mesmo Strings são objetos iráveis e podem retornar um Iterathor.
# Exemplo:

minha_string = 'banana'
meu_iterathor_2 = iter(minha_string)

print(next(meu_iterathor_2))
print(next(meu_iterathor_2))
print(next(meu_iterathor_2))
print(next(meu_iterathor_2))
print(next(meu_iterathor_2))
print(next(meu_iterathor_2))
