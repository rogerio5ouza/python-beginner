'''
TUPLAS

Tupla é uma coleção de dados ordenados e imutável. Em Python Tuplas são declaradas entre parênteses.
'''
tuplaFrutas = ('abacate', 'banana', 'caju')
print(tuplaFrutas)

# Acessando itens de uma Tupla

tuplaFrutas = ('abacate', 'banana', 'caju')
print(tuplaFrutas[1])

# Indices negativos (significa começar do fim, -1 refere-se ao último item, -2 ao segundo último item e etc.)

tuplaFrutas = ('abacate', 'banana', 'caju')
print(tuplaFrutas[-1])

# Ordenar Indices (Range of Indexes) - Podemos definir uma ordem de índices, definindo onde iniciar e onde terminar.
# Quando definimos uma ordem, o valor de retorno sempre será uma nova Tupla com os itens especificados.
# Exemplo - (Retorna o terceiro, quarto e quinto item):

tuplaFrutas = ('abacate', 'banana', 'caju', 'melancia',
               'goiaba', 'manga', 'morango')
print(tuplaFrutas[2:5])

# Ordem negativa de índices (Range of Negative Indexes)
# Exemplo - (Retorna o item do índice -4 (incluído) até o índice -1 (excluído)):

tuplaFrutas = ('abacate', 'banana', 'caju', 'melancia',
               'goiaba', 'manga', 'morango')
print(tuplaFrutas[-4:-1])

'''
Alterar valores de uma tupla (Change Tuple Values)

Depois que uma tupla é criada, não podemos alterar seus valores. Tuplas são imutáveis imutáveis, como tmabém é chamando.

Mas há uma solução alternativa. Podemos converter uma tupla em lista, alterar a lista e converter a lista novamnete em uma tupla.
'''
# Exemplo:
x = ('abacate', 'pera', 'morango')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)

print(x)

# LOOP ATRAVÉS DE UMA TUPLA (Loop Through a Tuple)
# Podemos percorrer os itens de uma tupla usando o for loop.
# Exemplo:

tuplaFrutas = ('ameixa', 'banana', 'caqui')
for x in tuplaFrutas:
    print(x)

# VERIFICAR SE O ITEM EXISTE
# Para vereficarmos se um item específico está presente em uma tupla, usamos a palavra chave IN.
# Exemplo:

tuplaFrutas = ('ameixa', 'banana', 'caqui')
if 'banana' in tuplaFrutas:
    print('Success! Banana esta presente em tupla frutas.')

# COMPRIMENTO DE UMA TUPLA (Tuple Length)
# Para verificarmos quantos itens possui uma tupla, usamos o método LEN().
# Exemplo:

tuplaFrutas = ('ameixa', 'banana', 'caqui')
print(len(tuplaFrutas))

'''
ADIÇÃO DE ITENS (Add Items)
Uma vez que a tupla é criada, não podemos adicionar itens a ela. Tuplas são IMUTÁVEIS.
'''
# Exemplo:

tuplaFrutas = ('ameixa', 'banana', 'caqui')
tuplaFrutas[3] = 'morango'  # Isso vai retornar um TypeError.
print(tuplaFrutas)

'''
CRIAÇÃO DE UMA TUPLA COM UM ITEM (Create Tuple With One Item)
Para criar uma tupla com apenas um item, podemos adicionar uma vírgula depois do item, caso contrário, o Python não reconhecerá como uma tupla.
'''
# Exemplo:

tuplaFrutas = ('ameixa',)
print(type(tuplaFrutas))

# Não é uma tupla

tuplaFrutas = ('ameixa')
print(type(tuplaFrutas))
