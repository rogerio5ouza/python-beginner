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
