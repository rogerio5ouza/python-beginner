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

'''
Adicionando itens (Adding Items)

A adição de um item ao dicionário é feita usando uma nova chave de índice e atribuindo um valor e ela.
'''

# Exemplo:

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}
dicio_carros['cor'] = 'grafiti'
print(dicio_carros)

# O método pop() remove o item de um valor de chave específica

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

dicio_carros.pop('marca')
print(dicio_carros)

# O método popitem() remove o último item inserido.

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

dicio_carros.popitem()
print(dicio_carros)

# A palavra-chave del remove o item com o nome da chave especificado.

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

del dicio_carros['marca']
print(dicio_carros)

# O método clear() esvazia o dicionário

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

dicio_carros.clear()
print(dicio_carros)

'''
Copiar um dicionário (Copy a Dictionary)

Não podemos copiar um dicionário simplesmente digitando dicio_carros_1 = dicio_carros_2, porque dicio_carros_2 será apenas uma referência
ao dicio_carros_1, e as alterações feitas no dicio_carros_1 também serão feitas do dicio_carros_2.

Existem maneiras de se fazer uma cópia, uma maneira é usar o bult-in copy() do dicionário.
'''
# Exemplo:

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2020'
}

meu_dicionario = dicio_carros.copy()
print(meu_dicionario)

# Outra maneira de se fazer cópia, é com uso da função bult-in dict():

dicio_carros = {
    'marca': 'Ford',
    'modelo': 'Fiesta',
    'ano': '2021'
}

meu_dicionario = dict(dicio_carros)
print(meu_dicionario)

'''
Dicionários aninhados (Nested Dictionaries)

Um dicionário também pode conter muitos dicionários.
'''
# Exemplo:

meus_cursos_programacao = {
    'beginner': {
        'HTML': '5',
        'horas': 100

    },
    'intermediate': {
        'JavaScript': 'ES6',
        'horas': 200
    },
    'advanced': {
        'Python': '3',
        'horas': 300
    }
}

print(meus_cursos_programacao)

# Podemos ainda, aninhar três dicionários que já existem como dicionários:

beginner = {
    'HTML': '5',
    'horas': 100

}

intermediate = {
    'JavaScript': 'ES6',
    'horas': 200
}

advanced = {
    'Python': '3',
    'horas': 300
}

meus_cursos_programacao_2 = {
    'beginner': beginner,
    'intermediate': intermediate,
    'advanced': advanced
}

print(meus_cursos_programacao_2)

'''
O construtor dict() (The dict() Constructor)

Também é possível usar o construtor dict() para criar um novo dicionário.
'''
# Exemplo:

dicio_carros = dict(marca='Ford', modelo='Fusion', year=2020)

print(dicio_carros)
