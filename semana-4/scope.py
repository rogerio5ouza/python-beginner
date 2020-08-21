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

'''
Global Scope

Uma variável criada no corpo principal do código Python é uma variável global e pertence ao escopo global.

Variáveis globais estão disponíveis em qualquer escopo, global e local.
'''
# Exemplo
# Uma variável criada fora de uma função é global e pode ser usada por qualquer pessoa:

x = 300


def minha_funcao_3():
    print(x)


minha_funcao_3()

print(x)

'''
Naming Variables

Se nós operarmos com o mesmo nome de variável dentro e fora de uma função, p Python as trarará como duas variáveis separadas,
uma dispinível no escopo global (fora da função) e outra disponível no escopo local (dentro da função).
'''
# Exemplo
# A função imprimirá o x local e,em seguida, o código imprimirá o x global:

x = 200


def minha_funcao_4():
    x = 300
    print(x)


minha_funcao_4()
print(x)
