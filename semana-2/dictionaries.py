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

# Uso do método values(), para retornar os valores de um dicionário:

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

for x in dicio_carros.values():
    print(x)

# Uso do método items(), para retornar as chaves e os valores de um dicionário:

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

for x, y in dicio_carros.items():
    print(x, y)

'''
Verifica se a chave existe (Check if Key Exists)

Para sabermos se uma chave específica se encontra no dicionário, usamos a keyword in. 
'''
# Exemplo:

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

if 'ano' in dicio_carros:
    print("Sim, 'ano' e uma chave do dicionario dicio_carros.")


'''
Comprimento do dicionário (Dictinary Length)

Para sabermos quantos itens (pares de chaves-valores) um dicionario possui, usamos a funcao len().
'''

# Exemplo:

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

print(len(dicio_carros))
