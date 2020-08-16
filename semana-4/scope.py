'''
Python Scope

Uma variável está disponível apenas dentro da área em que foi criada. Isso é chamado de Escopo.

Escopo Local

Uma variável criada dentro de uma função pertence ao escopo local dessa função e só pode ser usada dentro dessa função.
'''
# Exemplo
# Uma variável criada dentro de uma função está disponível apenas dentro dessa função:


def minha_função():
    x = 100
    print(x)


minha_função()
