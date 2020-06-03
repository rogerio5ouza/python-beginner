'''
Python Booleans

Booleans representa um de dois valores: True ou False.

Valores Booleanos

Quando você compara dois valores, a expressão é avaliada e o Python retorna a resposta Booleana.
'''
# Exemplo:

print(10 > 9)
print(10 == 9)
print(10 < 9)

'''
Quando executmaos uma condição em uma instrução IF, o Python retorna True ou False.
'''
# Exemplo:

a = 200
b = 33

if b > a:
    print('b é maior do que a')
else:
    print('b não é maior do que a')


'''
Evaluate Values and Variables (Avaliar valores e variáveis)

A função bool() permite avaliar qualquer valor e retornar True ou False.
'''
# Exemplo:
# Avalia uma string e um número:

print(bool('Hello'))
print(bool(15))

# Avalia duas variáveis:

x = 'Hello'
y = 15

print(bool(x))
print(bool(y))

'''
A maioria dos valores é True

Quase todo valor é avaliado como True se tiver algum tipo de conteúdo.
Qualquer cadeia é True, exceto cadeias vazias.
Qualquer número é True, exceto 0.
Qualquer lista, tupla, conjunto e dicionário são True, exceto os vazios.
'''
# Exemplo:
bool('abc')
bool(123)
bool(['apple', 'cherry', 'banana'])

'''
Alguns valores são falsos

De fato, não há muitos valores avaliados como Falso, exceto valores vazios, como (), [], {}, "", o número 0 e o valor Nenhum.
E claro, o valor Flase avalia como False.
'''
# Exemplo:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

'''
Mais um valor, ou objeto, nesse caso, é avaliado como False, ou seja, se você tiver um objeto que é feito de uma classe com 
uma função __len__ que retorna 0 ou False.
'''
# Exemplo:


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))

# Funções podem retornar um valor Booleano
# Você pode criar funções que retornem um valor Booleano
# Exemplo:


# def myFunction():
# return True


print(myFunction())

# Você pode executar o código com base na resposta Booleana de uma fumção.
# Exemplo: (Imprima 'YES!' se a função retornar True, ou então imprima 'NO!'):


def myFunction():
    return True


if myFunction():
    print('YES!')
else:
    print('NO!')

'''
O Python também possui muitas funções internas que retornam um valor Booleano, como a função isintance(),
que pode ser usada para determinar se um objeto é de um determinado tipo de dados:
'''
# Exemplo
# Verifica se um objeto é um número inteiro ou não:

x = 200
print(isinstance(x, int))
