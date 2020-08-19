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

'''
Function Inside Function

Conforme visto acima, a variável x não está disponível fora da função, mas está disponível para qualquer função dentro da função.
'''
# Exemplo
# A variável local pode ser acessada de uma função dentro da função:


def minha_funcao_2():
    x = 200

    def minha_funcao_interna():
        print(x)
    minha_funcao_interna()


minha_funcao_2()
