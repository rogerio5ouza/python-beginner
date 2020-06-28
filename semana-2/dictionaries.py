'''
Dicionários (Dictionaries)

Um dicionário é uma coleção não ordenada de itens, mutáveis e classificaveis. Em Python dicionários são escritos entre colchetes,
e  possuem vlaores e chaves.
'''
# Exemplo:

dicionario_carros = {
    'marca': 'fiat',
    'modelo': 'argo',
    'year': '2020'
}

print(dicionario_carros)

# Acessando itens - Podemos acessar itens através do nome da chave:

dicionario_carros = {
    'marca': 'fiat',
    'modelo': 'argo',
    'year': '2020'
}

modelo_carro = dicionario_carros['modelo']

print(modelo_carro)

# Há também o método get() que podemos utilizar para acessar os itens de uma chave:

dicionario_carros = {
    'marca': 'fiat',
    'modelo': 'argo',
    'year': '2020'
}

modelo_carro = dicionario_carros.get('marca')

print(modelo_carro)

'''
Alterar Valores (Change Values)

Podemos alterar um valor de um item específico, referindo-se ao seu nome de chave.
'''
# Exemplo:

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

dicio_carros['modelo'] = 'Corsa'
print(dicio_carros)


'''
Loop em um dicionário (Loop Through a Dictionary)

Usamos o loop for para percorrer um dicionário.
Ao percorrer um dicionário, o valor retornado é a chave do dicionário, mas existem métodos para retornar os valores também.
'''

# Retornando chaves de um dicionário:

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

for x in dicio_carros:
    print(x)

# Retornando valores de chave de um dicionário:

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

for x in dicio_carros:
    print(dicio_carros[x])
