'''
O que é um Módulo?

Consideramos um Módulo igual a uma biblioteca de código.
Um arquivo contendo um conjunto de funções que podemos incluir em nossos arquivos.
'''
# Exemplo:
# Vamos salvar esse código com o nome do arquivo meu_modulo.py:


import modules as mx


def boas_vindas(name):
    print("Ola, " + name)


'''
Variáveis no Módulo

O módulo pode conter funções e variáveis de todos os tipos (arrays, dicionários, objetos etc.).
'''
pessoa_1 = {
    "nome": "Joao",
    "idade": 32,
    "cidade": "Brasilia"
}
