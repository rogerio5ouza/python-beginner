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
