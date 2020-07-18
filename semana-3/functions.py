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

# Se o número de argumentos da keyword for desconhecido, adicionamos um duplo ** antes do nome do parâmetro:


def func_tipos_transporte_2(**transporte):
    print('Meu transporte preferido é' + transporte['terrestre'])


func_tipos_transporte_2(aquatico='barco', aereo='aviao', terrestre='bicicleta')

'''
Keyword Arguments (Argumentos de palavras-chave)

Podemos ainda passar argumentos com a sintaxe: key = valeu.
Dessa forma a ordem dos arguentos não importa.
'''
# Exemplo:


def meusFilhos(filho3, filho2, filho1):
    print('O caçula é o ' + filho3)


meusFilhos(filho1='José', filho2='Tomas', filho3='Torvalds')

'''
Default Parameter Value (Valor padrão do parâmetro)

Se chamarmos uma função sem argumento, ela usará um valor padrão.
'''
# Exemplo:


def func_nacionalidade(pais='Brasil'):
    print('Eu sou do (a) ' + pais)


func_nacionalidade('Dinamarca')
func_nacionalidade('India')
func_nacionalidade()
func_nacionalidade('Grecia')

'''
Passing a List as an Argument (Passando uma lista como argumento)

Podemos enviar qualquer tipo de argumento de dados para uma função (string, número, lista, dicionário, etc...) que será tratado com o mesmo tipo
de dados dentro da função.

Podemos enviar uma lista como argumento, que ainda será uma lista quando atingir a função.
'''
# Exemplo:


def func_comida(food):
    for x in food:
        print(x)


frutas = ['banana', 'manga', 'laranja']

func_comida(frutas)

'''
Return Values (Retornar valores)

Para permitir que uma função retorne um valor, usamos o comando return.
'''
# Exemplo:


def func_multiplica(x):
    return 10 * x


print(func_multiplica(2))
print(func_multiplica(5))
print(func_multiplica(10))
