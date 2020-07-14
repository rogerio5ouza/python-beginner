'''
Functions

Uma função é um bloco de de código que só é executado quando é chamado.
Podemos passar dados, conhecidos como parâmetros, para uma função.
Uma função pode retornar dados como resultado.
'''
# Exemplo:


def minha_function():
    print('Olá, da minha função!')


minha_function()

'''
Arguments (Argumentos)

Uma informação pode ser passada para uma função como argumento.
Argumentos são definidos depois do nome da função, entre parênteses. Podemos adicionar quantos argumentos quisermos, basta apenas separá-los com uma vírgula.
'''
# Exemplo:


def nomeCompleto(nome):
    print(nome + ' Souza')


nomeCompleto('Rogerio')
nomeCompleto('Carol')
nomeCompleto('Hermano')

'''
Numbers of Arguments (Números de argumentos)

Por padrão, uma função deve ser chamada com o número correto de argumentos. Isso significa que, se uma função espera receber 2 argumentos, devemos chamar 
a função com 2 argumentos, nem mais nem menos.
'''
# Exemplo:


def nomeCompleto(nome, sobrenome):
    print(nome + ' ' + sobrenome)


nomeCompleto('Hermano', 'Souza')
