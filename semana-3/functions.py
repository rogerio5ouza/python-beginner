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


def nomeCompleto_2(nome, sobrenome):
    print(nome + ' ' + sobrenome)


nomeCompleto_2('Hermano', 'Souza')

'''
Arbitrary Arguments, *args (Argumentos arbitrários)

Quando não soubermos quantos argumentos serão passados para uma função, adicionamos um * antes do nome do parâmetro na definição da função.
Dessa forma, a função receberá uma tupla de argumentos e poderá acessar os itens de acordo.
'''
# Exemplo:

def func_tipos_transporte(*transporte):
    print('Meu transporte preferido é' + transporte[2])

func_tipos_transporte('Aquatico', 'Aereo', 'Terrestre')

'''
Keyword Arguments (Argumentos de palavras-chave)

Podemos ainda passar argumentos com a sintaxe: key = valeu.
Dessa forma a ordem dos arguentos não importa.
'''
# Exemplo:

def meusFilhos(filho3, filho2, filho1):
    print('O caçula é o ' + filho3)

meusFilhos(filho1 = 'José', filho2= 'Tomas', filho3 = 'Torvalds')