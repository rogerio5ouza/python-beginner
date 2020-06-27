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
