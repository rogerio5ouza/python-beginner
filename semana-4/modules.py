'''
O que é um Módulo?

Consideramos um Módulo igual a uma biblioteca de código.
Um arquivo contendo um conjunto de funções que podemos incluir em nossos arquivos.
'''
# Exemplo:
# Vamos salvar esse código com o nome do arquivo meu_modulo.py:


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

'''
Nomeando um Módulo

Podemos nomear o arquivo do módulo como quisermos, mas deve ter a extensão de arquivo .py.

Podemos criar um alias ao importar um módulo, usando a keyword as.
'''
# Exemplo:
